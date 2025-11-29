import numpy as np

#O job assingment problem é formulado atraves de uma matriz quadrada,#
# ja que teremos exatamente uma pessoa para resolver cada tarefa

def executarSistema():
    print("\n\nPROBLEMA DE ASSOCIAÇÃO DE TAREFAS")
    n = int(input("Digite a Dimensão da Matriz NxN: "))
    custo = np.zeros((n, n)) #matriz com os custos

    print()
    for i in range(n):
        for j in range(n):
            custo[i][j] = float(input(f"Digite o custo em [pessoa {i + 1}][tarefa {j + 1}]: "))
    imprimirMatriz(custo)

    solucao = branchAndBound(custo)
    imprimirSolucao(solucao)

def imprimirSolucao(solucao):
    print("\nMelhor Solução Encontrada:")

    for pessoa, tarefa in enumerate(solucao[0]):
        print(f"Pessoa P{pessoa+1} -> Tarefa T{tarefa+1}")

    print(f"Custo total: {solucao[1]:.2f}\n\n")

def imprimirMatriz(custo):
    n = len(custo)

    print("\nMatriz de Custos digitada:\n")
    print("       ", end="")
    T = "T"
    #cabecalho das tarefas
    for j in range(n):
        print(f"{T:>6}{j+1}", end="") #>7 utilizado para alinhamento
    print()

    #linhas com as pessoas
    for i in range(n):
        print(f"P{i+1:<5}", end=" ")  #nome alinhado a esquerda
        for j in range(n):
            print(f"{custo[i][j]:>7.2f}", end="")  #float alinhado
        print()

#funcao lowerbound do pseudocodigo (lb)
#serve para calcular uma estimativa otimista do custo minimo da configuracao parcial
#descarta solucoes nao otimas
def calcularLimiteInferior(custo, atribuicoes, pessoa_atual):
    n = len(custo)
    custo_atual = 0;
    tarefas_disponiveis = list(range(n))

    #somando os custos das atribuicoes
    for pessoa, tarefa in enumerate(atribuicoes):
        if tarefa != -1:
            custo_atual += custo[pessoa][tarefa]
            tarefas_disponiveis.remove(tarefa)

    #soma o menor custo possivel para as pessas ainda nao atribuidas
    for pessoa in range(pessoa_atual, n):
        if pessoa < len(atribuicoes) and atribuicoes[pessoa] != -1:
            continue

        #comecamos com uma representacao infinita para o valor inicial nao influenciar nas atribuicoes
        minimo = np.inf
        #percoorre as tarefas disponiveis e encontra a com menor custo
        for tarefa in tarefas_disponiveis:
            if custo[pessoa][tarefa] < minimo:
                minimo = custo[pessoa][tarefa]

        if minimo != np.inf:
            custo_atual += minimo

    return custo_atual

#verifica se a tarefa ja foi atribuida
def verificarConsistencia(atribuicoes, tarefa):
    if tarefa in atribuicoes:
        return False
    return True

def calcularCustoCompleto(custo, atribuicoes):
    custo_total = 0

    for pessoa, tarefa in enumerate(atribuicoes):
        custo_total += custo[pessoa][tarefa]

    return custo_total

def branchAndBound(custo):
    n = len(custo)
    inicial = [-1] * n #cria uma lista (te tamnaho n) de -1s

    #F é um par de configuracao-custo
    #entao temos que F é [-1, -1, ...] (estado inicial), com custo 0
    F = []
    F.append((inicial, 0))


    melhor_custo = np.inf
    melhor_solucao = []
    i = 0

    #enquanto existir elementos em F
    while len(F) > 0:
        i += 1

        #remove a primeira configuracao da fila
        configuracao_atual, pessoa_atual = F.pop(0)

        if pessoa_atual == n:
            custo_atual = calcularCustoCompleto(custo, configuracao_atual)
            if custo_atual < melhor_custo:
                melhor_custo = custo_atual
                #faz a copia da lista, sem copy() as duas variaveis "apontariam" para a mesma lista
                melhor_solucao = configuracao_atual.copy()
            continue

        for tarefa in range(n):
            #verifica consitencia da confiuguracao
            if verificarConsistencia(configuracao_atual, tarefa) == True:
                #cria nova configuracao
                nova_configuracao = configuracao_atual.copy()
                nova_configuracao[pessoa_atual] = tarefa

                limite_inferior = calcularLimiteInferior(custo, nova_configuracao, pessoa_atual + 1)

                #realiza poda
                #so adiciona se um novo melhor cusato foi encontrado
                if limite_inferior < melhor_custo:
                    F.append((nova_configuracao, pessoa_atual + 1))

    #cria um par solucao-custo, para os melhor custo encontrado
    solucao = (melhor_solucao, melhor_custo)
    return solucao
