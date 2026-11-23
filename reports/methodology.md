# Metodologia

## Fontes do exercício

O projeto parte de cinco materiais fornecidos:

1. `Data_Analytics.ipynb` — notebook didático com inspeção, filtros, visualização, agregações, agrupamentos e merge das bases;
2. `Notebook_Professor.ipynb` — exercícios sobre médias por município, quantidade de inscritos, tipo de escola, gênero e missing;
3. `dados_enem_2021_BA.csv`;
4. `dados_enem_2021_BA_questoes_socieconomicas.csv`;
5. `Dicion_rio_Microdados_Enem_2021.xlsx`.

## Pergunta analítica

Como a participação e o desempenho dos registros do ENEM 2021 na Bahia variam segundo renda familiar, tipo de escola, cor/raça, escolaridade dos responsáveis, acesso digital e município de aplicação da prova?

## Junção

As duas bases possuem 266.194 registros e `NU_INSCRICAO` único. A junção 1:1 preserva os 266.194 registros.

## Notas ausentes

Notas ausentes não são imputadas. A ausência de nota aparece junto a faltas e eliminações nas variáveis de presença; imputar média ou mediana produziria resultados artificiais.

As análises de participação usam todos os 266.194 registros. As comparações de desempenho usam 174.793 registros com as cinco notas disponíveis.

## Indicador sintético

`MEDIA_SIMPLES_5` é a média aritmética de Ciências da Natureza, Ciências Humanas, Linguagens, Matemática e Redação.

Ela é um indicador criado exclusivamente para comparação descritiva neste projeto. Não é uma nota oficial do ENEM e não incorpora pesos de cursos.

## Tipo de escola

`TP_ESCOLA = 1` significa "Não respondeu". Comparações entre escola pública e privada usam apenas `TP_ESCOLA = 2` e `TP_ESCOLA = 3`.

## Município

`NO_MUNICIPIO_PROVA` é município de aplicação da prova. Não deve ser interpretado automaticamente como município de residência ou da escola.

## Seleção da amostra

A proporção de registros com as cinco notas disponíveis varia entre grupos socioeconômicos. Portanto, as diferenças de notas são comparações entre participantes com notas observadas, não efeitos causais.

## Causalidade

O estudo é descritivo. Diferenças de médias indicam associação/composição entre grupos e não demonstram que renda, raça, escola, acesso digital ou escolaridade dos responsáveis causem determinado desempenho.
