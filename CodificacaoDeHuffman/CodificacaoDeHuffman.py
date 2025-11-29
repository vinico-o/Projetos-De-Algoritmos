import heapq
from collections import Counter

"""
Codificação de Huffman para compressão de um texto fornecido pelo usuário
com um algoritmo guloso.

Explicação da codificação de Huffman:
1. Conta a frequência de cada caractere no texto (em binário).
    ou seja 0 - 00
            1 - 01
            2 - 10
            3 - 11
             ...
2. Cria uma árvore binária onde os caracteres menos frequentes estão mais profundos.
    

3. Gera códigos binários para cada caractere com base na posição na árvore. 
    resultado do programa - compressão de um texto em um código bin.


Não confundir:
   não é a codificação clássica tipo:
    a -> 00
    b -> 01
    c -> 10
      ...
    
    o valor binário de cada carac depende da freq no texto e do heapq (arv)

material auxiliar: ime-usp
                   wikipedia
    
"""

class noH:

    # O método construtor em Python é __init__ -> obrigatório para inicializar atributos
    def __init__(self, simbolo, frequencia): 
        self.simbolo = simbolo #caractere
        self.frequencia = frequencia #freq do caractere ou a soma deles
        self.esq = None
        self.dir = None
    
    # Compara a frequência de dois nós -> obrigatorio para o heapq
    def __lt__(self, other):
        # Compara apenas a frequência
        return self.frequencia < other.frequencia



def codificacaoDeHuffman(frequencias):
    
    heap = []
    
    for simbolo, freq in frequencias.items():
        
        no = noH(simbolo, freq)

        # o heapq organiza automaticamente os nós com base na frequência -> 
        # Como o nó tem o método __lt__, apenas fazemos o push do nó na heap
        heapq.heappush(heap, no)
        

    while len(heap) > 1:
        
        # heapq.heappop() é igual ao pop de pilha -> só que remove o menr elemento
        no1 = heapq.heappop(heap) 
        no2 = heapq.heappop(heap) 
        
        
        # ccria um novo no com a soma das freq
        novoNo = noH(None, no1.frequencia + no2.frequencia)
        novoNo.esq = no1
        novoNo.dir = no2
        
        
        # add o novo nó no heap (dps de apontar para os filhos)
        heapq.heappush(heap, novoNo)
        
    
    # dá pop (remove) o nó raiz da arv
    return heapq.heappop(heap)


def gerarCodHuffman(no, prefixo = "", cod = None):
    
    # esse prefixo vai guardando o código binário e somando conforme desce na arv
    # soma 0 se for para a esq
    # soma 1 se for para a dir

    if cod is None:
        cod = {}
    
    # parte gulosa do algoritmo
    if no is not None:
        
        # se o nó é folha, passa o simbolo e o cod bin
        if no.simbolo is not None:
            cod[no.simbolo] = prefixo
            
        
        # vai pra esquerda 
        if no.esq != None:
            gerarCodHuffman(no.esq, prefixo + "0", cod)

        # vai pra direita
        if no.dir != None:
            gerarCodHuffman(no.dir, prefixo + "1", cod)
            
    
    return cod

def textoCodHuffman(texto):
    
    # freq de cada caractere
    frequencia = Counter(texto)

    # cria a arv de Huffman e os códigos binários para cada caractere 
    raiz = codificacaoDeHuffman(frequencia)

    # retorna os cod de cada caractere
    cod = gerarCodHuffman(raiz)
    
    
    codParaCaracteres = []
    
    for c in texto:
        codParaCaracteres.append(cod[c])

    # "".join() -> transforma a lista numa string com tudo (texto codificado)
    return cod, "".join(codParaCaracteres)



# apenas printa os valores binarios de cada letra e dps o texto codificado em bin
def resultados(textoOriginal, cod, textoCodificado):
    
    print (f"\nTexto Original: {textoOriginal}")

    print("\nResultados:")
    
    print ("\nLetra em binário:")
    for s in cod:
        print(f"{s} -> {cod[s]}")

    print(f"\nCodificação de Huffman: {textoCodificado}")

def executarSistema():
    # main
    entrada = input("-----Informe o texto para Codificação de Huffman-----\n->> ")
    codigos, texto_codificado = textoCodHuffman(entrada)


    resultados(entrada, codigos, texto_codificado)