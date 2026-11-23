from __future__ import annotations

import pandas as pd

SCORE_COLS = [
    "NU_NOTA_CN",
    "NU_NOTA_CH",
    "NU_NOTA_LC",
    "NU_NOTA_MT",
    "NU_NOTA_REDACAO",
]


def validate_unique_registration(df: pd.DataFrame) -> None:
    if "NU_INSCRICAO" not in df.columns:
        raise ValueError("NU_INSCRICAO não encontrada.")
    if df["NU_INSCRICAO"].duplicated().any():
        raise ValueError("NU_INSCRICAO duplicada na base.")


def merge_enem_socioeconomic(
    enem: pd.DataFrame,
    socioeconomic: pd.DataFrame,
) -> pd.DataFrame:
    validate_unique_registration(enem)
    validate_unique_registration(socioeconomic)
    return enem.merge(
        socioeconomic,
        on="NU_INSCRICAO",
        how="inner",
        validate="one_to_one",
    )


def complete_score_sample(df: pd.DataFrame) -> pd.DataFrame:
    data = df.dropna(subset=SCORE_COLS).copy()
    data["MEDIA_SIMPLES_5"] = data[SCORE_COLS].mean(axis=1)
    data["MEDIA_OBJETIVAS"] = data[SCORE_COLS[:-1]].mean(axis=1)
    return data
