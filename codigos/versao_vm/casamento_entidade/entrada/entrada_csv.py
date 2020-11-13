import pandas as pd
from dedupe._typing import Data
from pandas import DataFrame


def df_para_dict(df: DataFrame) -> Data:
    """Converte DataFrame para Dicionário (RecordPairs from dedupe).

    Parameters
    ----------
    :param df: DataFrame
        DataFrame com dados a serem convertidos.

    Returns
    ----------
    :return dados_dedupe: RecordPairs
        Dados no tipo Dicionário (RecordPairs).
    """
    df = df.where(pd.notnull(df), None)  # dedupe soh aceita None
    dados_dedupe = df.to_dict(orient="index")  # dedupe soh aceita dict

    return dados_dedupe
