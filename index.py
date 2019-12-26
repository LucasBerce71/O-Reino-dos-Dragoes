import random
import time

def displayIntro():
    print('O reino dos dragões')
    print('========================================================================================')
    print('Você está perdido em uma terra cheia de dragões de várias espécies, e precisa dar um jeito de ir embora, para isso você tem que achar a chave do portal dessa terra ')
    print('que se encontra em uma das duas cavernas localizadas nessa terra. Na sua frente, você avista essas duas cavernas, em uma das cavernas ')
    print('habita um dragão tranquilo que está com a chave irá deixar você entrar e ir embora com ela (chave), ')
    print('e dentro da outra caverna habita um dragão que não tem a chave e se você entrar lá ele mmata você, e o pior é que você não sabe em qual caverna o dragão com a chave habita!')
    print('=========================================================================================')

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Em qual caverna você vai se arriscar entrar para procurar a chave? (A PRIMEIRA = DIGITE 1 | A SEGUNDA = DIGITE 2')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('Você vai se aproximando da caverna escolhida...')
    time.sleep(2)
    print('Está muito escuro e assustador...')
    time.sleep(2)
    print('Ele abriu a mandíbula e...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Cuspiu a chave do portal para você! Você fez a escolha certa!!!')
    else:
        print('Game Over! Você entrou na caverna errada e o dragão matou você!!!')

playAgain = 'SIM'
while playAgain == 'SIM' or playAgain == 'sim':
    
    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Deseja jogar novamente? (SIM ou NÃO)')
    playAgain = input()

    if playAgain == 'NÂO' or 'NAO' or 'não' or 'nao':
        print('Obrigado por jogar O REINO DOS DRAGÕES! Em breve vem uma nova versão do jogo. Créditos ao desenvolvedor do jogo:')
        print(' LUCAS BERCÊ DE JESUS')
        break