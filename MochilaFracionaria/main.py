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
import numpy as np

def mochilaFracionaria(itens, capacidadeMax):

    # precisamos ordenar por valor/peso
    #   como o algoritmo pega sempre o maior valor/peso 
    #   ordenar dessa maneira, mostra os itens que tem maior valor/peso até o menor valor/peso
    #   já é um indicativo de quais escolher primeiro
    itensOrdenados = sorted(itens, key=lambda x: x[2]/x[1], reverse=True)

    valorTotal = 0
    pesoAtual = 0

    matriz_solucao = np.zeros((3, 3), dtype=object)
    i = 0

    # percorrendo os itens ja ordenados
    for nome, peso, valor in itensOrdenados:

        # se da pra colocar o item inteiro - apenas add
        if peso + pesoAtual <= capacidadeMax:
            pesoAtual += peso
            valorTotal += valor
            matriz_solucao[i][0] = nome 
            matriz_solucao[i][1] = peso
            matriz_solucao[i][2] = valor
        

        # se nao da pra colocar o item inteiro - fracionamos
        else:
            valorFracionado = (capacidadeMax - pesoAtual) * (valor / peso) 
            valorTotal += valorFracionado 
            matriz_solucao[i][0] = nome 
            matriz_solucao[i][1] = capacidadeMax - pesoAtual 
            matriz_solucao[i][2] = valorFracionado 
            pesoAtual = capacidadeMax 
            
            break
    
        i += 1

    return matriz_solucao, valorTotal

def resultados(matriz_solucao, valorTotal):

    print("---------\nItens escolhidos (peso x valor):")
    
    for i in range(matriz_solucao.shape[0]):
        
        if matriz_solucao[i][0] != 0:
            
            print(f"{matriz_solucao[i][0]} -> {matriz_solucao[i][1]} x {matriz_solucao[i][2]:.2f}")

    print (f"\nValor total: {valorTotal:.2f}")
    print("---------\n")

# main

itens = [('A',random.randint(50, 120), random.randint(10, 30)),
         ('B',random.randint(50, 120), random.randint(10, 30)),
         ('C',random.randint(50, 120), random.randint(10, 30)),]

capacidadeMaxima = random.randint(100, 300)

print ("\n\n---------\nIdeia do algoritmo: pegar o maior valor possivel dentro da capacidade da mochila\n" \
        "se tem espaço - pega o item com maior valor/peso\n" \
        "se não conseguir pegar inteiro - pega uma parte\n---------\n" )

print ("Capacidade x valor")
for i in itens:
    print(f"{i[0]} -> {i[1]}  x {i[2]} -> valor/peso: {i[2]/i[1]:.2f}")

print (f"\nCapacidade maxima da mochila: {capacidadeMaxima}\n")

matriz_solucao, valorTotal = mochilaFracionaria(itens, capacidadeMaxima)

resultados(matriz_solucao, valorTotal)