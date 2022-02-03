import os

def primeira_velha():
    a=[]
    c=1
    for i in range(1,4):
        b=[]
        for j in range(1,4):
            print(f'{c} |', end=' ')
            b.append(str(c))
            c+=1
        a.append(b)
        print()
        print('-'*11)
    return a    

def mudar_jogador(simb):
    if simb=='X':
        simb='O'
    else:
        simb='X'
    return simb

def jogar_velha(simb, jog, matriz):
    try:
        for i in matriz:
            for j in i:
                if j==jog:
                    troc=list(map(lambda x: x.replace(j, simb), i))
                    matriz.insert(matriz.index(i), troc)
                    matriz.remove(i)
                    val=True
                    break
        return val
    except UnboundLocalError:
        val=False
        return val

def mostrar_velha(matriz):
    for i in matriz:
        for j in i:
            print(f'{j} |', end=' ')
        print()
        print('-'*11)

def teste(matriz):
    terminou=False

    # Jogos em linhas
    for i in range(0,3):
        if matriz[i][0]==matriz[i][1] and matriz[i][1]==matriz[i][2]:
            terminou=True

    # Jogos em colunas
    for j in range(0,3):
        if matriz[0][j]==matriz[1][j] and matriz[1][j]==matriz[2][j]:
            terminou=True

    # Jogos em diagonais
    if matriz[0][0]==matriz[1][1] and matriz[1][1]==matriz[2][2]:
        terminou=True
    if matriz[2][0]==matriz[1][1] and matriz[1][1]==matriz[0][2]:
        terminou=True

    # Jogos em Velha
    velha=0
    for i in range(0,3):
        for j in range(0,3):
            if matriz[i][j]=='X' or matriz[i][j]=='O':
                velha+=1
    if velha==9:
        terminou=True

    return terminou

matriz=primeira_velha()
simb='X'

while True:
    val=False
    while val==False:
        jog=input(f'Em qual posição deseja colocar o  [{simb}]? ')
        val=jogar_velha(simb, jog, matriz)
        os.system('cls') or None
        if val==False:
            print('JOGADA INVÁLIDA! Tente novamente!')
            print()
        mostrar_velha(matriz)
    simb=mudar_jogador(simb)
    
    terminou=teste(matriz)

    if terminou:
        print('JOGO FINALIZADO')
        break