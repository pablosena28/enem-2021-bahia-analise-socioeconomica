import pandas as pd
import pytest

from src.data_preparation import SCORE_COLS, complete_score_sample, merge_enem_socioeconomic


def sample_main():
    return pd.DataFrame(
        {
            "NU_INSCRICAO": [1, 2],
            "NU_NOTA_CN": [500.0, None],
            "NU_NOTA_CH": [510.0, 520.0],
            "NU_NOTA_LC": [520.0, 530.0],
            "NU_NOTA_MT": [530.0, 540.0],
            "NU_NOTA_REDACAO": [600.0, 620.0],
        }
    )


def sample_socio():
    return pd.DataFrame(
        {
            "NU_INSCRICAO": [1, 2],
            "Q006": ["B", "C"],
        }
    )


def test_merge_is_one_to_one():
    result = merge_enem_socioeconomic(sample_main(), sample_socio())
    assert len(result) == 2


def test_merge_rejects_duplicate_registration():
    socio = pd.concat([sample_socio(), sample_socio().iloc[[0]]], ignore_index=True)
    with pytest.raises(ValueError):
        merge_enem_socioeconomic(sample_main(), socio)


def test_complete_score_sample_excludes_missing_score():
    merged = merge_enem_socioeconomic(sample_main(), sample_socio())
    result = complete_score_sample(merged)
    assert result["NU_INSCRICAO"].tolist() == [1]


def test_simple_mean_is_arithmetic_mean_of_five_scores():
    merged = merge_enem_socioeconomic(sample_main(), sample_socio())
    result = complete_score_sample(merged)
    expected = sum([500.0, 510.0, 520.0, 530.0, 600.0]) / 5
    assert result.loc[0, "MEDIA_SIMPLES_5"] == expected


def test_score_columns_expected():
    assert len(SCORE_COLS) == 5
