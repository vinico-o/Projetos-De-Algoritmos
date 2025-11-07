#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <limits.h>
#include <stdbool.h>

int TAMANHO;
int custoMAX = UINT_MAX;



typedef struct b
{
    int custo;
    int *vetor;

}b;

typedef struct{

    b *b;
    b *prox;

}no;

typedef struct {

    no *inicio;


}Fila;


void incializar(b *solucao)
{
    solucao->vetor = malloc(sizeof(TAMANHO));
    solucao->custo = custoMAX;

    for (int i = 0; i < TAMANHO; i++)
    {
        solucao->vetor[i] = 0;
    }
}

void gerarMatrizAleatoria(int **matriz)
{
    matriz = malloc(sizeof(int));

    for (int i = 0; i < TAMANHO; i++)
    {
        matriz[i] = malloc(sizeof(int));
    }
    
    for (int i = 0; i < TAMANHO; i++)
    {
        for (int j = 0; j < TAMANHO; j++)
        {
            matriz[i][j] = rand() % 20 + 1;
        }
    }
}

bool verificarConsistencia(b *solucao)
{
    for (int i = 0; i < TAMANHO; i++)
    {
        int pessoa = solucao->vetor[i];
        int posicao = i;

        for (int j = 0; j < TAMANHO; j++)
        {   
            if (solucao->vetor[j] == pessoa && j != posicao && solucao->vetor[i] != 0)
            {
                return false;
            }
        }
    }

    return true;

}



void imprimirMatriz()
{

}



void inserirNaFila (Fila *f, int novaPessoa)
{

}

void gerandoFilaSolucao()
{








}


int calcularCusto(no* no, int** matriz)
{
    int soma = 0;
    for(int i = 0; i < TAMANHO; i++)
    {
        soma += matriz[no->b->vetor[i] - 1][i];
    }

    return soma;
}

int main ()
{
    srand(time(NULL));

    TAMANHO = rand() % 10;

    int **matriz;
    b *solucao;

    gerarMatrizAleatoria(matriz);

/*     calcularCusto(); */

    return 0;
}