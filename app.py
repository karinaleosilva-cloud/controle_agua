""" Sistema de Monitoramento dos níveis de um reservatório de água."""

import datetime
from colorama import Fore, init

init(autoreset=True)

def registrar_nivel_reservatorio():
    print("🐍 === Sistema de Monitoramento do Reservatório 💧 ===")
    
    try:
        # 1. Coleta de dados (sua lógica original, com tratamento de exceção)
        nivel_atual = float(input("💧 Digite o nível atual do reservatório em metros: "))
        nivel_maximo = float(input("💧 Digite o nível máximo do reservatório em metros: "))

        # 2. Validação inicial e prevenção de anomalias críticas (sua lógica aprimorada)
        if nivel_maximo <= 0:
            print("Erro de Configuração: O nível máximo do reservatório deve ser maior que zero.")
            return
            
        if nivel_atual < 0:
            print("Alerta de Sensor: Leitura inválida. O nível de água não pode ser negativo!")
            return
            
        if nivel_atual > nivel_maximo:
            print(f"ALERTA CRÍTICO: Transbordamento detectado! Nível atual ({nivel_atual}m) excede o limite físico ({nivel_maximo}m).")
            return

        # 3. Cálculo da porcentagem de preenchimento
        porcentagem = (nivel_atual / nivel_maximo) * 100

        # 4. Uso de Listas para mapear os níveis
        # Cada item da lista é uma tupla contendo (limite_percentual_superior, classificacao)
        # Assumimos uma divisão igualitária de 20% para cada um dos 5 níveis.
        tabela_niveis = [
            (20.0, "🔴 1 - Muito Baixo", Fore.RED),
            (40.0, "🟡 2 - Baixo", Fore.YELLOW),
            (60.0, "🟢 3 - Médio", Fore.GREEN),
            (80.0, "🔷 4 - Alto", Fore.CYAN),
            (100.0, "🔵 5 - Muito Alto", Fore.BLUE)
        ]

        # 5. Lógica de classificação iterando sobre a lista
        classificacao_atual = ""
        cor_classificacao = ""
        for limite, descricao, cor in tabela_niveis:
            if porcentagem <= limite:
                classificacao_atual = descricao
                cor_classificacao = cor
                break # Encerra o loop assim que encontra a faixa correta

        # 6. Geração do registro (log) com a biblioteca datetime
        momento_leitura = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # 7. Saída de dados formatada
        print("\n" + "="*40)
        print("          RELATÓRIO DE STATUS          ")
        print("="*40)
        print(f"Data/Hora da Leitura : {momento_leitura}")
        print(f"Volume Preenchido    : {porcentagem:.2f}%")
        print(f"Classificação        : {cor_classificacao}Nível {classificacao_atual}")
        print("="*40)

    except ValueError:
        # Tratamento caso o usuário digite texto em vez de números
        print("Erro de Entrada: Por favor, insira apenas valores numéricos válidos (ex: 2.5).")

# Executa o programa
if __name__ == "__main__":
    registrar_nivel_reservatorio()
    