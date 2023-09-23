from random import  randint
from time import sleep
dados = str(input('Aperte ENTER para rolar os dados e Batalhar! '))
enemyList = ['Bandido', 'Ogro', 'Morto-vivo', 'Lobo-Gigante']
inimigo = randint(0, 2)
sleep(1)
if inimigo == 0: # Bandido
    print(f'Seu adversário é um {enemyList[inimigo]}.')
    print('ROLANDO DADOS...')
    sleep(1)
    print('GERANDO FICHA DE INIMIGO...')
    sleep(1)
    con_i = randint(4, 6)
    fr_i = randint(6, 8)
    dex_i = randint(5, 7)
    agi_i = randint(5, 7)

elif inimigo == 1: # Ogro
    print(f'Seu adversário é um {enemyList[inimigo]}.')
    print('ROLANDO DADOS...')
    sleep(1)
    print('GERANDO FICHA DE INIMIGO...')
    sleep(1)
    con_i = randint(4, 6)
    fr_i = randint(6, 8)
    dex_i = randint(5, 7)
    agi_i = randint(5, 7)

elif inimigo == 2: # Morto-vivo
    print(f'Seu adversário é um {enemyList[inimigo]}.')
    print('ROLANDO DADOS...')
    sleep(1)
    print('GERANDO FICHA DE INIMIGO...')
    sleep(1)
    con_i = randint(4, 6)
    fr_i = randint(6, 8)
    dex_i = randint(5, 7)
    agi_i = randint(5, 7)

elif inimigo == 3: # Lobo-gigante
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
print('=-' * 5 + ' FICHA DO ADVERSÁRIO ' + '=-' * 5 )
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