# 🐍💧 Sistema de Monitoramento do Reservatório

Aplicação em Python 🐍 para monitorar o nível de um reservatório de água 💧, calcular o percentual de preenchimento e classificar o nível com mensagens coloridas no terminal.

## Requisitos

- Python 3.8 ou superior
- Biblioteca `colorama`

Instale a dependência com:

```bash
pip install colorama
```

## Como executar

No diretório do projeto, execute:

```bash
python app.py
```

Informe o nível atual e o nível máximo do reservatório em metros. O programa exibirá um relatório com a data e hora da leitura, o percentual preenchido e a classificação correspondente.

## Classificação dos níveis

| Percentual preenchido | Nível | Situação | Cor |
| --- | --- | --- | --- |
| Até 20% | 🔴 Nível 1 | Muito baixo | Vermelho |
| Acima de 20% até 40% | 🟡 Nível 2 | Baixo | Amarelo |
| Acima de 40% até 60% | 🟢 Nível 3 | Médio | Verde |
| Acima de 60% até 80% | 🔷 Nível 4 | Alto | Ciano |
| Acima de 80% até 100% | 🔵 Nível 5 | Muito alto | Azul |

## Validações

O programa informa um erro quando:

- O nível máximo é menor ou igual a zero.
- O nível atual é negativo.
- O nível atual ultrapassa o nível máximo.
- Os valores informados não são numéricos.

## Exemplo

```text
💧 Digite o nível atual do reservatório em metros: 2.5
💧 Digite o nível máximo do reservatório em metros: 5

Volume Preenchido    : 50.00%
Classificação        : 🟢 Nível 3 - Médio
```
