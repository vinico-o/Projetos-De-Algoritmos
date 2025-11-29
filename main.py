import AssociacaoDeTarefas.AssociacaoDeTarefas as adt
import CodificacaoDeHuffman.CodificacaoDeHuffman as cdh
import MochilaBooleana.MochilaBooleana as mb
import MochilaFracionaria.MochilaFracionaria as mf
import SubsequenciaComumMaxima.SubsequenciaComumMaxima as scm

def menu():
    print("MENU DO SISTEMA")
    print("01 - Associação De Tarefas")
    print("02 - Codificação de Huffman")
    print("03 - Mochila Booleana")
    print("04 - Mochila Fracionária")
    print("05 - Subsequência Comum Máxima")
    print("00 - Sair\n")

escolha = 99

while escolha != 0:
    menu()
    escolha = int(input("Escolha uma das opções abaixo: "))
    if escolha == 1:
        adt.executarSistema()

    if escolha == 2:
        cdh.executarSistema()

    if escolha == 3:
        mb.executarSistema()

    if escolha == 4:
        mf.executarSistema()

    if escolha == 5:
        scm.executarSistema()