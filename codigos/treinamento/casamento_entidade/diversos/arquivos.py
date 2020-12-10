import json
import shutil
from pathlib import Path
from typing import Dict, Union


def conversao_path(arq_or_dir: Union[Path, str]) -> Path:
    """Converte uma string para tipo Path (se necessário).

    Parameters
    ----------
    :param arq_or_dir: Union[Path, str]
        Arquivo/diretório a ser convertido.

    Returns
    ----------
    :return arq_or_dir: Path
        Retorna o diretorio/arquivo no tipo Path.
    """
    if not isinstance(arq_or_dir, str):
        return arq_or_dir
    else:
        return Path(arq_or_dir)


def criar_dir(diretorio: Union[Path, str], forcar: bool = False) -> None:
    """Cria um diretorio.

    Cria um diretório e seus parentes (se não estiverem criados). Se forcar=True,
    então o diretorio é excluído para criar um novo.

    Parameters
    ----------
    :param diretorio: Union[Path, str]
        Diretorio a ser criado, do tipo Path (pathlib).
    :param forcar: bool
        Especifica se é para excluir o diretorio se já existir.

    Returns
    ----------
    :return: None
    """
    diretorio = conversao_path(diretorio)
    try:
        diretorio.mkdir(parents=True)
    except FileExistsError:
        if forcar:
            shutil.rmtree(diretorio)
            diretorio.mkdir(parents=True)
    return None


def salvar_json(arquivo_json: Union[Path, str], dados_json: Dict, encoding: str = "utf-8",
                ensure_ascii: bool = False, indent: int = 4) -> None:
    """Salva JSON em arquivo.

    Parameters
    ----------
    :param arquivo_json: Union[Path, str]
        Nome do arquivo JSON (juntamente com diretorio).
        E.g.: /home/user/arquivo.json
    :param dados_json: Dict
        Dados JSON para salvamento.
    :param encoding: str, default="uft-8"
        Tipo de codificação.
    :param ensure_ascii: boolean, default=False
        Parâmetro de json.dump.
    :param indent: int, default=4
        Parâmetro de json.dump.

    Returns
    ----------
    :return: None
    """
    arquivo_json = conversao_path(arquivo_json)
    with arquivo_json.open(mode="w+", encoding=encoding) as file:
        json.dump(dados_json, file, ensure_ascii=ensure_ascii, indent=indent)
    return None


def carregar_json(arquivo_json: Union[Path, str]) -> Dict:
    """Carrega arquivo JSON em dict (dicionário python).

    Parameters
    ----------
    :param arquivo_json: Union[Path, str]
        Nome do arquivo JSON (juntamente com diretorio).
        E.g.: /home/user/arquivo.json

    Returns
    ----------
    :return dados_json: Dict
        Dados do arquivo JSON.
    """
    arquivo_json = conversao_path(arquivo_json)
    with arquivo_json.open(mode='r') as file:
        dados_json = json.load(file)
    return dados_json
