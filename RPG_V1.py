from random import randint
from time import sleep


print('-=' * 20)
print('=-' * 6 + ' RPG ADVENTURE ' + '=-' * 6 )
print('-=' * 20)

# Historia parte 1

print('Você é encontrado por um viajante, preso em uma cela de uma antiga prisão...')
#sleep(1.5)
print('O viajante te coloca em sua carroça e te leva até a cidade mais proxima...')
#sleep(1.5)
print('Você acorda e se depara com o prefeito da cidade...')
#sleep(1.5)
print('PREFEITO: Quem é você? ')
#sleep(2)

# Criação do personagem
def createPlayer():
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
createPlayer()
def createEnemy():
    dados = str(input('Aperte ENTER para rolar os dados e Batalhar! '))
    enemyList = ['Bandido', 'Ogro', 'Morto-vivo', 'Lobo-Gigante']
    inimigo = randint(0, 2)
    sleep(1)
    if inimigo == 0:  # Bandido
        print(f'Seu adversário é um {enemyList[inimigo]}.')
        print('ROLANDO DADOS...')
        sleep(1)
        print('GERANDO FICHA DE INIMIGO...')
        sleep(1)
        con_i = randint(4, 6)
        fr_i = randint(6, 8)
        dex_i = randint(5, 7)
        agi_i = randint(5, 7)

    elif inimigo == 1:  # Ogro
        print(f'Seu adversário é um {enemyList[inimigo]}.')
        print('ROLANDO DADOS...')
        sleep(1)
        print('GERANDO FICHA DE INIMIGO...')
        sleep(1)
        con_i = randint(4, 6)
        fr_i = randint(6, 8)
        dex_i = randint(5, 7)
        agi_i = randint(5, 7)

    elif inimigo == 2:  # Morto-vivo
        print(f'Seu adversário é um {enemyList[inimigo]}.')
        print('ROLANDO DADOS...')
        sleep(1)
        print('GERANDO FICHA DE INIMIGO...')
        sleep(1)
        con_i = randint(4, 6)
        fr_i = randint(6, 8)
        dex_i = randint(5, 7)
        agi_i = randint(5, 7)

    elif inimigo == 3:  # Lobo-gigante
        print(f'Seu adversário é um {enemyList[inimigo]}.')
        print('ROLANDO DADOS...')
        sleep(1)
        print('GERANDO FICHA DE INIMIGO...')
        sleep(1)
        con_i = randint(4, 6)
        fr_i = randint(6, 8)
        dex_i = randint(5, 7)
        agi_i = randint(5, 7)

    # FICHA DO PERSONAGEM
    print('-=' * 20)
    print('=-' * 5 + ' FICHA DO ADVERSÁRIO ' + '=-' * 5)
    print('-=' * 20)
    atk_i = (con_i + fr_i + dex_i + agi_i) / 2
    dfs_i = (con_i + fr_i + dex_i + agi_i) / 3
    print(f'NOME:        {enemyList[inimigo]}')
    print(f'CONTITUIÇÂO: {con_i}')
    print(f'FORÇA:       {fr_i}')
    print(f'DESTREZA:    {dex_i}')
    print(f'AGILIDADE:   {agi_i}')
    print(f'ATAQUE:      {atk_i:.1f}')
    print(f'DEFESA:      {dfs_i:.1f}')

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


# Destino - batalhe ou continue
dados = input('Pressione ENTER para rolar os dados e descobrir seu destino!')
print('ROLANDO DADOS...')
sleep(3)
destino = randint(1, 2)
if destino == 1:
    print('Você encontrou um inimigo, prepare-se para a BATALHA!')
elif destino == 2:
    print('Seu caminho está livre, siga em frente!')







# definir atributos inimigos
# criar combate
# criar itens





