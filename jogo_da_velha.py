import os

contador = 0
simbolo = 'X'
endereco = 0
vrau = False
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
acabou = False
jogada_invalida = False
erro = 0
fim_do_jogo = False
deu_empate = False
cor = 'não'


# Atualiza a minha matriz a cada loop
def nova_tabela():
    print('===========================')
    print('|J O G O   D A   V E L H A|')
    print('===========================')

    print(' ','=' * 23)
    print(f'  |  {lista[0][0]} |   | {lista[0][1]} |   | {lista[0][2]}  |')
    print(' ','=' * 23)
    print(f'  |  {lista[1][0]} |   | {lista[1][1]} |   | {lista[1][2]}  |')
    print(' ','=' * 23)
    print(f'  |  {lista[2][0]} |   | {lista[2][1]} |   | {lista[2][2]}  |')
    print(' ','=' * 23)

# Fica alternando entre X e O
def troca_simbolo(a,b):
    if b == 'sim':
        if a == '\033[1;31mX\033[m':
            a = '\033[1;36mO\033[m'
        else:
            a = '\033[1;31mX\033[m'
    else:
        if a == 'X':
            a = 'O'
        else:
            a = 'X'
    return a
# Verificador de coluna
def verifica_coluna(acabou):
    
    contador = 0
    for l in range(0, 2):
        if lista[l][0] == lista[l + 1][0]:
            contador += 1
        if contador == 2:
            acabou = True
            
    contador = 0
    for l in range(0, 2):
        if lista[l][1] == lista[l + 1][1]:
            contador += 1
        if contador == 2:
            acabou = True
            
    contador = 0
    for l in range(0, 2):
        if lista[l][2] == lista[l + 1][2]:
            contador += 1
        if contador == 2:
            acabou = True

    return acabou

# verifica linha
def verifica_linha(acabou):
    contador = 0
    for l in range(0, 2):
        if lista[0][l] == lista[0][l + 1]:
            contador += 1
        if contador == 2:
            acabou = True
    contador = 0
    for l in range(0, 2):
        if lista[1][l] == lista[1][l + 1]:
            contador += 1
        if contador == 2:
            acabou = True
    contador = 0      
    for l in range(0, 2):
        if lista[2][l] == lista[2][l + 1]:
            contador += 1
        if contador == 2:
            acabou = True  
      
    return acabou

# verifica diagonal <Principal>
def verifica_diagonal(acabou):
    contador = 0
    for l in range(0, 2):
        if lista[l][l] == lista[l + 1][l + 1]:
            contador += 1
        if contador == 2:
            acabou = True

    return acabou

# verifica diagonal <inversa>
def diagonal_inversa(acabou):
    if lista[0][2] == lista[1][1] and lista[2][0] == lista[1][1]:
        acabou = True

    return acabou

# verifica empate
def empate(deu_empate):
    z = 0
    for l in range(0, 3):
        for c in range(0, 3):
            if type(lista[l][c]) == str:
                z += 1 
    if z == 9:
        deu_empate = True

    return deu_empate

print('''
 ================================================
|       B E M   V I N D O   J O G A D O R        |
|       =================================        |
|                                                |
| Em qual sistema você está rodando este código? |
|                                                |
| [ 1 ] - Linux                                  |
| [ 2 ] - Windows                                |
|                                                |
 ================================================''')
hype = int(input('Digite o número da opção desejada: '))
if hype == 1:
    escolha = 'clear'
elif hype == 2:
    escolha = 'cls'
print('''
==========================================================================
| Você está rodando este código no "Visual Studio Code"? [Sim / Não]:    |
==========================================================================''')
cor = input('Digite [Sim / Não]: ').lower().strip()
if cor == 'sim':
    simbolo = '\033[1;31mX\033[m'


limpatela = lambda: os.system(escolha)
while True:
    limpatela()
    nova_tabela()
    while True:
        erro = 0
        print()
        endereco = int(input(f'Digite onde você deseja jogar o [ {simbolo} ] ? '))     
        for l in range (0, 3):
            for c in range (0, 3):
                if endereco == lista[l][c] and type(lista[l][c] == int):
                    lista[l][c] = simbolo
                else:
                    erro += 1
        if erro == 9:
            print(('Jogada inválida, tente novamente.'))
            break
        limpatela()
        nova_tabela()
        simbolo = troca_simbolo(simbolo, cor)
        fim_do_jogo = verifica_coluna(acabou)

        if fim_do_jogo != True:
            fim_do_jogo = verifica_linha(acabou)
        if fim_do_jogo != True:
            fim_do_jogo = verifica_diagonal(acabou)
        if fim_do_jogo != True:
            fim_do_jogo = diagonal_inversa(acabou)
        if fim_do_jogo != True:
            fim_do_jogo = empate(deu_empate)
            deu_empate = empate(deu_empate)
        if deu_empate == True:
            print('Deu empate')
        if fim_do_jogo == True:
            print('Saindo...')
            exit()
        