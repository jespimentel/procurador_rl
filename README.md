# Quando serei Procurador de Justiça?

A regressão linear é uma técnica de machine learning, do tipo aprendizado supervisionado.

É bastante usada em problemas de regressão, isto é, aqueles em que se deseja fazer previsões a partir de dados conhecidos do passado.

Nessa brincadeira, tentamos encontrar a relação linear entre as variáveis "ano de ingresso na carreira" e "tempo decorrido até a promoção", extraídas da lista de antiguidade mais recente (01/2025), usando a função `polyfit` da biblioteca `numpy`.

O modelo busca um padrão dos dados, mas não captura a complexidade da movimentação da carreira, que pode ser intuída no gráfico abaixo:

![Ingresso x Tempo até a promoção](img/plot_tempo_promoção.png)

Os valores do coeficiente angular e intecepto encontrados são, respectivamente, 1.0987068177853268 e -2159.4368249111044.

A fórmula de cálculo usada na aplicação é, portanto:

```python 
resultado = (int(ano_de_ingresso * 1.0987068177853268 -2159.4368249111044 + ano_de_ingresso))
```

Confira o código em: https://github.com/jespimentel/perfil_mpsp/blob/main/perfil_membros_mpsp_2024_01.ipynb


Abraços!

Pimentel
