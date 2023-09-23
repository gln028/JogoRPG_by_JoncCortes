from time import sleep
from random import randint

player = str(input('Digite o nome do seu HERÓI: '))
classeList = ['Guerreiro', 'Caçador', 'Mago', 'Ladrão']
print('''Escolha sua Classe:
[ 0 ] Guerreiro
[ 1 ] Caçador
[ 2 ] Mago
[ 3 ] Ladrão''')
classe = int(input('Sua Escolha: '))
sleep(1)
if classe == 0: # Guerreiro
    print(f'Olá {player} você escolheu a classe {classeList[classe]}.')
    input('Precione ENTER para gerar seus atributos: ')
    print('ROLANDO DADOS...')
    sleep(1)
    print('GERANDO FICHA DE PERSONAGEM...')
    sleep(1)
    con = randint(4, 6)
    fr = randint(6, 8)
    dex = randint(5, 7)
    agi = randint(5, 7)
elif classe == 1: # Caçador
    print(f'Olá {player} você escolheu a classe {classeList[classe]}.')
    input('Precione ENTER para gerar seus atributos: ')
    print('ROLANDO DADOS...')
    sleep(1)
    print('GERANDO FICHA DE PERSONAGEM...')
    sleep(1)
    con = randint(5, 7)
    fr = randint(4, 6)
    dex = randint(6, 8)
    agi = randint(5, 7)
elif classe == 2: # Mago
    print(f'Olá {player} você escolheu a classe {classeList[classe]}.')
    input('Precione ENTER para gerar seus atributos: ')
    print('ROLANDO DADOS...')
    sleep(1)
    print('GERANDO FICHA DE PERSONAGEM...')
    sleep(1)
    con = randint(8, 10)
    fr = randint(3, 5)
    dex = randint(5, 7)
    agi = randint(4, 6)
elif classe == 3: # Ladrão
    print(f'Olá {player} você escolheu a classe {classeList[classe]}.')
    input('Precione ENTER para gerar seus atributos: ')
    print('ROLANDO DADOS...')
    sleep(1)
    print('GERANDO FICHA DE PERSONAGEM...')
    sleep(1)
    con = randint(3, 5)
    fr = randint(2, 4)
    dex = randint(6, 8)
    agi = randint(7, 9)
else:
    print('OPÇÂO INVALIDA!')

# FICHA DO PERSONAGEM
print('-=' * 20)
print('=-' * 5 + ' FICHA DO PERSONAGEM ' + '=-' * 5 )
print('-=' * 20)
atk = (con + fr + dex + agi) / 2
dfs = (con + fr + dex + agi) / 3
print(f'NOME:        {player}')
print(f'CLASSE:      {classeList[classe]}')
print(f'CONTITUIÇÂO: {con}')
print(f'FORÇA:       {fr}')
print(f'DESTREZA:    {dex}')
print(f'AGILIDADE:   {agi}')
print(f'ATAQUE:      {atk:.1f}')
print(f'DEFESA:      {dfs:.1f}')
sleep(2)
