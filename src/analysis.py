from pathlib import Path

import pandas as pd

from src.data_preparation import SCORE_COLS, complete_score_sample, merge_enem_socioeconomic

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "data" / "source" / "dados_enem_2021_BA.csv"
SOCIO = ROOT / "data" / "source" / "dados_enem_2021_BA_questoes_socieconomicas.csv"


def main() -> None:
    main_cols = [
        "NU_INSCRICAO",
        "TP_COR_RACA",
        "TP_ESCOLA",
        "NO_MUNICIPIO_PROVA",
        "TP_PRESENCA_CN",
        "TP_PRESENCA_CH",
        "TP_PRESENCA_LC",
        "TP_PRESENCA_MT",
        *SCORE_COLS,
    ]
    socio_cols = ["NU_INSCRICAO", "Q001", "Q002", "Q006", "Q024", "Q025"]

    enem = pd.read_csv(MAIN, usecols=main_cols)
    socio = pd.read_csv(SOCIO, usecols=socio_cols)

    merged = merge_enem_socioeconomic(enem, socio)
    complete = complete_score_sample(merged)

    print("=== ENEM 2021 | BAHIA ===")
    print(f"Registros: {len(merged):,}")
    print(f"Cinco notas disponíveis: {len(complete):,} ({len(complete)/len(merged):.2%})")
    print(f"Presença CH/LC: {(merged['TP_PRESENCA_CH'] == 1).mean():.2%}")
    print(f"Presença CN/MT: {(merged['TP_PRESENCA_CN'] == 1).mean():.2%}")

    print("\n=== MÉDIAS | AMOSTRA COM CINCO NOTAS ===")
    print(complete[SCORE_COLS + ["MEDIA_SIMPLES_5"]].mean().round(2).to_string())

    print("\n=== RENDA FAMILIAR | MÉDIA SIMPLES ===")
    print(
        complete.groupby("Q006")["MEDIA_SIMPLES_5"]
        .agg(["count", "mean", "median"])
        .round(2)
        .to_string()
    )


if __name__ == "__main__":
    main()
