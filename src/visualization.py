from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "reports" / "figures"


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)

    income = pd.read_csv(PROCESSED / "renda_desempenho.csv")

    fig, ax = plt.subplots(figsize=(13, 6))
    ax.plot(income["Q006"], income["media_simples"], marker="o", linewidth=2)
    ax.set_title("Média simples das cinco notas por faixa de renda familiar")
    ax.set_xlabel("Categoria Q006")
    ax.set_ylabel("Média simples das cinco notas")
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIGURES / "renda_desempenho.svg", bbox_inches="tight")
    plt.close(fig)

    race = pd.read_csv(PROCESSED / "raca_cor_desempenho.csv")
    race = race[race["RACA_CAT"] != "Não declarado"].sort_values("media_simples")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(race["RACA_CAT"], race["media_simples"])
    ax.set_title("Média simples das cinco notas por cor/raça declarada")
    ax.set_xlabel("Média simples das cinco notas")
    ax.grid(True, axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIGURES / "raca_cor_desempenho.svg", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
