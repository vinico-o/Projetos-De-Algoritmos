""" 

Problema da Subsequência Comum Máxima (Longest Common Subsequence) usando Programação Dinâmica

encontra a maior subsquencia em duas strings de entrada -> subsequencia mais longa com caracteres nas duas strings 
                                                                e na mesma ordem

material auxiliar -> pseudocodigo dos slides
                  -> geek for geeks
"""


def subsequenciaComumMaxima(entrada1, entrada2):
    
    tam1 = len(entrada1)
    tam2=  len(entrada2)

    # matriz solução de programação dinâmica
    # tam1 + 1 linhas e tam2 + 1 colunas
    matriz_solucao = [[0] * (tam2 + 1) for x in range(tam1 + 1)]
    
    # construindo a tabela começando por baixo
    for i in range(1, tam1 + 1):
        for j in range(1, tam2 + 1):
            
            # se os caracteres são iguais (indicio de possível subsequencia) - +1 
            if entrada1[i - 1] == entrada2[j - 1]:
                matriz_solucao[i][j] = matriz_solucao[i - 1][j - 1] + 1
            
            # se são diferentes, pega o maior valor das células próximas
            else:
                matriz_solucao[i][j] = max(matriz_solucao[i - 1][j], matriz_solucao[i][j - 1])
    
    # retorna o comprimento da maior subsequencia
    return matriz_solucao[tam1][tam2]


def executarSistema():
    entrada1 = input("\nInforme a primeira string: ")
    entrada2 = input("\nInforme a segunda string: ")
    resultado = subsequenciaComumMaxima(entrada1, entrada2)
    print (f"\nSubsequencia: {resultado}\n\n")


