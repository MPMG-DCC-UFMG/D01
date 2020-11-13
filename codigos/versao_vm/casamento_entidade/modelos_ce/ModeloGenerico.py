import abc
from typing import Dict, Optional
from dedupe._typing import Data

class ModeloGenerico(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def treinamento(self, dados_treinamento: Data):
        pass

    @abc.abstractmethod
    def casamento_entidade(self, dados_casamento: Data, threshold: Optional[float]):
        pass
