import sys
import counttime
import time


def Inicializa(numeroDeSlots):
    return [[] for _ in range(numeroDeSlots)]

def Hash(Chave):
    Som = 0
    Conta = 1
    for Index in Chave:
        Som += (ord(Index) * Conta)
        Conta += 1
    return Som * 19

def MakeHash(Chave):
    return Hash(Chave) % len(hash_table)

def ArquivoSaida(Saida):

    Local = 0
    for Slot in hash_table:
        if Slot:
            Local += 1
    Saida.write(str(Local) + '\n')

    Local = 0
    for Slot in hash_table:
        if Slot:
            Saida.write(str(Local)+':'+str(Slot) + '\n')
        Local += 1

def Pesquisar(Chave):

    HashKey = MakeHash(Chave)

    if hash_table[HashKey] == Chave:
        return True, HashKey, 1  # 1 É o custo da pesquisa, ou seja O(1)
    else:
        for Index in range(1, 19):
            HashKey = Hash(Chave) + (Index ** 2) + (23 * Index)
            HashKey = HashKey % len(hash_table)

            if hash_table[HashKey] == Chave:
                return True, HashKey, (Index + 1)
    return False, None, 0

def Remover(Chave):

    _Bool, HashKey, Custo = Pesquisar(Chave)
    if _Bool == True:
        print("Remover [" + Chave + "]")
        hash_table[HashKey] = []
        return Custo
    else:
        print("Chave Não Existe [" + Chave + "]")
        return Custo

def Inserir(Chave):

    if VerificaTamanhoString(Chave):
        return 0
    HashKey = MakeHash(Chave)
    Bucket = hash_table[HashKey]

    if Bucket == []:
        hash_table[HashKey] = (Chave)
        print('Inserido: \x1B[34m' + str(HashKey) +
              '\x1B[0m:\x1B[32m' + Chave + '\x1B[0m')
        return 1
    elif Bucket == Chave:
        print('Já Existe:[\x1B[34m' + str(HashKey) +
              '\x1B[0m:\x1B[32m' + Chave + '\x1B[0m]')
        return 0
    else:
        Bool, HashKey, Custo = TrataColisoes(Chave)
        if Bool:
            hash_table[HashKey] = Chave
            print('Inserido: \x1B[34m' + str(HashKey) +
                  '\x1B[0m:\x1B[32m' + Chave + '\x1B[0m')
            return Custo
        else:
            print("Impossível Inserir ["+Chave+"] . . .")
    return 0

def TrataColisoes(Chave):

    for Index in range(1, 20):
        HashKey = Hash(Chave) + (Index ** 2) + (23 * Index)
        HashKey = HashKey % len(hash_table)
        if VerificaPosicaoValida(HashKey):  # Um pois ni primeiro acesso já conta como O(1) + n
            return True, HashKey, Index + 1
    return False, None, 0  # Ultimo parâmetro é o total de acessos à tabela.

def VerificaPosicaoValida(HashKey):
    if hash_table[HashKey] == []:
        return True
    return False

def VerificaTamanhoString(Chave):
    if len(Chave) > 15:  # Condição específica do Trabalho
        print("Chave Inválida! [" + Chave + "]")
        return True
    return False

def writeTests(MediaCustoTotal, QtdADD, QtdDEL, CustoRemover, CustoInserir, FILE, Tempo, Name, QtdLinhas):

    FILE.write('Teste: '+Name+'\n' +
               'Média de Custo Total: '+str(MediaCustoTotal)+'\n'+
               'Quantidade Elementos: '+str(QtdLinhas)+'\n' +
               'Quantidade de ADD:' +str(QtdADD) + '\n' +
               'Quantidade de DEL:' +str(QtdDEL)+'\n' +
               'Custo Remover: '+str(CustoRemover)+'\n' +
               'Custo Inserir: '+str(CustoInserir)+'\n' +
               'Tempo de Execução: '+str(Tempo)+'\n'+
               ('-'*50)+'\n\n')

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Erro na entrada dos parâmetros!")
        exit(True)

    Entrada, Saida, Testes = open(sys.argv[1]), open(sys.argv[2], 'w'), open('Testes.txt', 'a')
    QtdTestes = int(Entrada.readline())

    for Index in range(QtdTestes):

        timeInit = time.time()  # Tempo inicial
        hash_table = Inicializa(101)  # A cada novo laço

        RemoverCusto = 0
        InserirCusto = 0
        QtdDEL       = 0
        QtdADD       = 0
        QtdElementos = 0
    
        # Essa linha está percorrendo a quantidade de linhas de cada teste
        QtdLinhas = int(Entrada.readline())
        for __ in range(QtdLinhas):

            Elemento = Entrada.readline()

            if Elemento[:3] == "DEL":
                QtdDEL += 1
                RemoverCusto += Remover(Elemento[4:].replace('\n', ''))
            else:
                QtdADD += 1
                InserirCusto += Inserir(Elemento[4:].replace('\n', ''))
            QtdElementos += 1
        writeTests( (RemoverCusto + InserirCusto) / QtdLinhas, QtdADD, QtdDEL, RemoverCusto, 
                    InserirCusto,Testes, 
                    counttime.Count(timeInit, time.time()), 
                    sys.argv[1], QtdLinhas)
        ArquivoSaida(Saida)
    Entrada.close
    Saida.close
