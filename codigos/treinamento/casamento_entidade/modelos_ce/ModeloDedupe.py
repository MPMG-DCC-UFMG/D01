import logging
from pathlib import Path
from typing import Union, List, Dict, Optional

import dedupe
from dedupe._typing import Clusters, Data

from .ModeloGenerico import ModeloGenerico
from ..diversos import criar_dir


class ModeloDedupe(ModeloGenerico):
    def __init__(self, campos_casamento: List[Dict], diretorio_modelo_dedupe: Union[Path, str] = "execucao_dedupe",
                 nome_arq_treino: Union[Path, str] = "arquivo_treinamento.json",
                 nome_arq_configuracao: Union[Path, str] = "arquivo_configuracao",
                 threshold: float = 0.5, num_cores: Optional[int] = None,
                 modelo_ce: Optional[dedupe.Dedupe] = None):
        self.campos_casamento = campos_casamento

        self.diretorio_modelo_dedupe = Path(diretorio_modelo_dedupe)
        criar_dir(diretorio_modelo_dedupe)
        self.arquivo_treino = Path(f"""{diretorio_modelo_dedupe}/{nome_arq_treino}""")
        self.arquivo_configuracao = Path(f"""{diretorio_modelo_dedupe}/{nome_arq_configuracao}""")
        self.threshold = threshold
        self.num_cores = num_cores

        self.modelo_ce = modelo_ce

    def __str__(self):
        return f"ModeloDedupe(diretorio_modelo_dedupe={self.diretorio_modelo_dedupe}, " \
               f"arquivo_treino={self.arquivo_treino}, arquivo_configuracao={self.arquivo_configuracao}, " \
               f"threshold={self.threshold}, num_cores={self.num_cores})"

    def __repr__(self):
        return f"ModeloDedupe(diretorio_modelo_dedupe={self.diretorio_modelo_dedupe}, " \
               f"arquivo_treino={self.arquivo_treino}, arquivo_configuracao={self.arquivo_configuracao}, " \
               f"threshold={self.threshold}, num_cores={self.num_cores})"

    def carregar_modelo_treinado(self) -> None:
        if self.arquivo_configuracao.exists():
            print(f"Carregando o modelo a partir do arquivo de configuração {self.arquivo_configuracao}")
            with self.arquivo_configuracao.open(mode="rb") as arquivo:
                self.modelo_ce = dedupe.StaticDedupe(settings_file=arquivo, num_cores=self.num_cores)
        else:
            print(f"O arquivo {self.arquivo_configuracao} não existe.")

    def treinamento(self, dados_treinamento: Data, sample_size: int = 15_000, blocked_proportion: float = 0.9,
                    original_length: Optional[int] = None, forcar_treinamento: bool = False) -> None:
        if (self.arquivo_configuracao.exists()) and (not forcar_treinamento):
            self.carregar_modelo_treinado()
        else:
            # Instanciação
            self.modelo_ce = dedupe.Dedupe(variable_definition=self.campos_casamento, num_cores=self.num_cores)

            # Preparando treino
            logging.info("Preparando o treinamento do modelo...")
            if self.arquivo_treino.exists():
                logging.info(f"\tLendo exemplos do arquivo de treinamento ({self.arquivo_treino}).")
                with self.arquivo_treino.open() as arquivo:
                    self.modelo_ce.prepare_training(data=dados_treinamento, training_file=arquivo,
                                                    sample_size=sample_size, blocked_proportion=blocked_proportion,
                                                    original_length=original_length)
            else:
                self.modelo_ce.prepare_training(data=dados_treinamento, training_file=None, sample_size=sample_size,
                                                blocked_proportion=blocked_proportion, original_length=original_length)

            # Active Learning
            logging.info("Iniciando o treinamento com Active Learning...")
            dedupe.console_label(self.modelo_ce)
            self.modelo_ce.train()

            # Salva configuração e exemplos de treino
            logging.info("Salvando os arquivos de treino e configuração...")
            self.__salva_treino()
            self.__salva_configuracao()

            # Liberando memória
            self.modelo_ce.cleanup_training()

    def casamento_entidade(self, dados_casamento: Data, threshold: Optional[float] = 0.5) -> Clusters:
        # Tenta carregar o modelo se ele não estiver instanciado
        if self.modelo_ce is None:
            self.carregar_modelo_treinado()
            if self.modelo_ce is None:
                raise ValueError("Precisa executar o método treinamento() para realizar a criação do modelo"
                                 "(se não existir criado).")

        return self.modelo_ce.partition(data=dados_casamento, threshold=threshold)

    def __salva_treino(self) -> None:
        with self.arquivo_treino.open(mode="w+") as arquivo:
            self.modelo_ce.write_training(file_obj=arquivo)

    def __salva_configuracao(self) -> None:
        with self.arquivo_configuracao.open(mode="wb+") as arquivo:
            self.modelo_ce.write_settings(file_obj=arquivo)
