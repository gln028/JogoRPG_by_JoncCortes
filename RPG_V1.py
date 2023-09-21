from random import randint
from time import sleep

print('-=' * 20)
print('=-' * 6 + ' RPG ADVENTURE ' + '=-' * 6 )
print('-=' * 20)

# Historia parte 1

print('Você é encontrado por um viajante, preso em uma cela de uma antiga prisão...')
sleep(1.5)
print('O viajante te coloca em sua carroça e te leva até a cidade mais proxima...')
sleep(1.5)
print('Você acorda e se depara com o prefeito da cidade...')
sleep(1.5)
print('PREFEITO: Quem é você? ')
sleep(2)

# Criação do personagem

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
    con = randint(6, 10)
    fr = randint(6, 10)
    dex = randint(6, 10)
    agi = randint(6, 10)
elif classe == 1: # Caçador
    print(f'Olá {player} você escolheu a classe {classeList[classe]}.')
    input('Precione ENTER para gerar seus atributos: ')
    print('ROLANDO DADOS...')
    sleep(1)
    print('GERANDO FICHA DE PERSONAGEM...')
    sleep(1)
    con = randint(6, 10)
    fr = randint(6, 10)
    dex = randint(6, 10)
    agi = randint(6, 10)
elif classe == 2: # Mago
    print(f'Olá {player} você escolheu a classe {classeList[classe]}.')
    input('Precione ENTER para gerar seus atributos: ')
    print('ROLANDO DADOS...')
    sleep(1)
    print('GERANDO FICHA DE PERSONAGEM...')
    sleep(1)
    con = randint(6, 10)
    fr = randint(6, 10)
    dex = randint(6, 10)
    agi = randint(6, 10)
elif classe == 2: # Ladrão
    print(f'Olá {player} você escolheu a classe {classeList[classe]}.')
    input('Precione ENTER para gerar seus atributos: ')
    print('ROLANDO DADOS...')
    sleep(1)
    print('GERANDO FICHA DE PERSONAGEM...')
    sleep(1)
    con = randint(6, 10)
    fr = randint(6, 10)
    dex = randint(6, 10)
    agi = randint(6, 10)
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

# Historia parte 2

print(f''' {player}: Sou um {classeList[classe]}, me chamo {player},
passei tanto tempo jogado naquela cela imunda, que já nem me lembro mais o motivo!''')
sleep(1.5)
print(f''' PREFEITO: Otimo {player}, Você pode se redimir de seus crimes
fazendo um trabalho para mim...''')
sleep(1.5)
print(f''' PREFEITO: O mercador precisa ir até a cidade vizinha, e precisa de uma escolta!
 Leve ele em segurança, e seus crimes estarão perdoados...''')
sleep(3)

print(' SUA JORNADA COMEÇA!')

# definir as classe, criar itens, criar monstros e combate.





