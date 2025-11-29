"""
Imagine um conjunto de objetos que eu gostaria de colocar na minha mochila. 
Cada objeto tem um certo peso e um certo valor. Posso escolher uma fração — entre 0% e 100% — de cada objeto para colocar na mochila. 
Minha mochila suporta no máximo 15kg. 
Que fração de cada objeto devo colocar na mochila de modo a maximizar o valor total?


INTENÇÃO: pegar o maior valor x peso possivel
          dentro da capacidade da mochila


material auxiliar: ime-usp
                   wikipedia
"""
import random


def mochilaFracionaria(itens, capacidadeMax):

    # precisamos ordenar por valor/peso
    #   como o algoritmo pega sempre o maior valor/peso 
    #   ordenar dessa maneira, mostra os itens que tem maior valor/peso até o menor valor/peso
    #   já é um indicativo de quais escolher primeiro
    itensOrdenados = sorted(itens, key=lambda x: x[2]/x[1], reverse=True)

    valorTotal = 0
    pesoAtual = 0

    matriz_solucao = []
    i = 0

    # percorrendo os itens ja ordenados
    for nome, peso, valor in itensOrdenados:

        # se da pra colocar o item inteiro - apenas add
        if peso + pesoAtual <= capacidadeMax:
            pesoAtual += peso
            valorTotal += valor
            matriz_solucao.append((nome, peso, valor))
        

        # se nao da pra colocar o item inteiro - fracionamos
        else:
            valorFracionado = (capacidadeMax - pesoAtual) * (valor / peso) 
            valorTotal += valorFracionado 
            matriz_solucao.append((nome, capacidadeMax - pesoAtual, valorFracionado))
            pesoAtual = capacidadeMax 
            
            break
    
        i += 1

    return matriz_solucao, valorTotal

def resultados(matriz_solucao, valorTotal):

    print("---------\nItens escolhidos (peso x valor):")
    
    for nome, peso, valor in matriz_solucao:
        
        print(f"{nome} -> {peso} x {valor:.2f}")

    print (f"\nValor total: {valorTotal:.2f}")
    print("---------\n")

# main
def executarSistema():
    print ("\n\n---------\nIdeia do algoritmo: pegar o maior valor possivel dentro da capacidade da mochila\n" \
            "se tem espaço - pega o item com maior valor/peso\n" \
            "se não conseguir pegar inteiro - pega uma parte\n---------\n" )


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

    matriz_solucao, valorTotal = mochilaFracionaria(itens, capacidadeMaxima)

    resultados(matriz_solucao, valorTotal)