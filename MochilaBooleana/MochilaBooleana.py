"""

Problema da Mochila Booleana (mochila 0-1 - em inglês, Knapsack Problem)
usando Programação Dinâmica

os itens não podem ser fracionados
0 - não incluído
1 - incluído

matriz resultado -> guarda as soluções -> ideia de programação dinâmica


materiais auxiliares: canal no youtube - Universo Discreto
                      o site geek for geeks tem um material sobre mochila booleana
                            porém nn usa programação dinâmica

"""
import random


def mochilaBooleana(capacidadeMax, itens):
    
    n = len(itens)

    # cria vetores de pesos_vet e valores_vet    
    pesos_vet = [itens[i][1] for i in range(n)]
    valores_vet = [itens[i][2] for i in range(n)]


    # cria a matriz resultado -> guarda as soluções
    # n + 1 linhas e capacidadeMax + 1 colunas, pois considera o caso base (0 itens ou capacidadeMax 0)
    matriz_resultado = []
    
    # criando matriz_resultado
    for _ in range(n + 1):
        
        linha = []
        
        for _ in range(capacidadeMax + 1):
            linha.append(0)
        
        matriz_resultado.append(linha)

    # preenche a matriz resultado
    # começa em 1, pois a linha 0 e coluna 0 representam o caso base (entt pula esse caso)
    for i in range(1, n + 1):
        for j in range(1, capacidadeMax + 1):

            # caso 1: pegar o item
            if pesos_vet[i - 1] > j:
                pegar = 0
            
            else:
                pegar = valores_vet[i - 1] + matriz_resultado[i - 1][j - pesos_vet[i - 1]]

            # caso 2: não pegar o item
            naoPegar = matriz_resultado[i - 1][j]

            # pega o maior valor e passa como resultado -> melhor caso
            matriz_resultado[i][j] = max(pegar, naoPegar)

    capacidadeMax_restante = capacidadeMax
    itens_escolhidos = []

    # pega os itens escolhdos (A, B, e/ou C) -> ajuda na visualização da resposta do algoritmo
    for i in range(n, 0, -1):

        # verifica se o item foi pego
        # se o item mudou de uma linha para a outra -> indica que a solução foi melhor
        if matriz_resultado[i][capacidadeMax_restante] != matriz_resultado[i - 1][capacidadeMax_restante]:
            
            # passa o item escolhido da solução
            itens_escolhidos.append(itens[i - 1])
            
            # subtrai a capacidade restanto pelo peso do item i-1
            capacidadeMax_restante -= pesos_vet[i - 1]

    # para ter a ordem correta, revertemos o vetor
    itens_escolhidos.reverse()

    return matriz_resultado[n][capacidadeMax], itens_escolhidos




# main
def executarSistema():
    print ("\n\n---------\nIdeia do algoritmo: pegar o maior valor possivel dentro da capacidadeMax da mochila\n" \
            "se tem espaço - pega o item com maior valor\n" \
            "se não conseguir pegar inteiro - não pega o item\n---------\n" )

    itens = []

    nomes = ['A', 'B', 'C']

    for nome in nomes:
        print(f"\nItem {nome}:")
        peso = int(input("Peso: "))
        valor = int(input("Valor: "))
        print()

        itens.append((nome, peso, valor))

    print("\n\nItem - peso - valor:")
    for item in itens:
        print(item)


    capacidadeMaxima = int(input("\nInforme a capacidade maxima da mochila: "))

    print (f"Capacidade maxima da mochila: {capacidadeMaxima}\n")

    resultado, itens_escolhidos = mochilaBooleana(capacidadeMaxima, itens)


    print (f"Valor total na mochila: {resultado}")
    print(f"Itens escolhidos (item - peso - valor): {itens_escolhidos}\n\n\n\n")
    
