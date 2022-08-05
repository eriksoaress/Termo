from random import randint

from unidecode import unidecode





# FUNÇÃO RETIRADA DO SITE STACKOVERFLOW (https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing)
import sys, time
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
    return ''






# VERIFICA SE A PALAVRA DO JOGADOR É VÁLIDA
def valida_palavra(palavras_lista, tentativas_contador):
    valida = False
    palavras_lista_sem_acento = [] # ARMAZENA A PALAVRA DO JOGADOR SEM OS ACENTOS
    while valida == False:
        jogador_palavra = input(print_slow('Digite uma palavra válida de 5 letras: '))
        jogador_palavra = jogador_palavra.lower() 
        for palavra in palavras_lista:
            palavras_lista_sem_acento.append(unidecode(palavra))
        if len(jogador_palavra) == 5 and unidecode(jogador_palavra) in palavras_lista_sem_acento and tentativas_contador <= 6:
            valida = True
    return jogador_palavra





# FUNÇÃO PARA PEGAR UMA PALAVRA ALEATÓRIA DO BANCO DE PALAVRAS
def sorteia_palavra(palavras_lista): 
    indice = randint(0,len(palavras_lista))
    palavra = palavras_lista[indice]
    return palavra






def verifica_letras(palavra, jogador_palavra, tentativas_contador, tentativas,teclado):
    contador_letras = {} # ARMAZENA QUANTAS VEZES A LETRA JÁ APARECEU
    verificacao = [] # ARMAZENA A SITUAÇÃO DAS LETRAS (AMARELO, VERDE, CINZA)
    for letra in jogador_palavra:
        verificacao.append(letra.upper())


    for indice in range(0,len(jogador_palavra)):
        if unidecode(jogador_palavra[indice]) == unidecode(palavra[indice]): # SE A LETRA DA PALAVRA ESTIVER PRESENTE E NA ORDEM CERTA VAI RECEBER VERDE
            verificacao[indice] = f'\033[7;32;40m {palavra[indice].upper()} \033[m'
            if unidecode(jogador_palavra[indice]) not in contador_letras:
                contador_letras[unidecode(jogador_palavra[indice])] = 1
            else:
                contador_letras[unidecode(jogador_palavra[indice])] += 1
            if unidecode(jogador_palavra[indice].upper()) not in teclado[0]:
                teclado[0].append(unidecode(jogador_palavra[indice].upper()))
                if unidecode(jogador_palavra[indice].upper()) in teclado[1]:
                    index = teclado[1].index(unidecode(jogador_palavra[indice].upper()))
                    del teclado[1][index]




    for indice in range(0,len(jogador_palavra)):
        if unidecode(jogador_palavra[indice]) in unidecode(palavra) and unidecode(jogador_palavra[indice]) != unidecode(palavra[indice]): # SE A LETRA DA PALAVRA ESTIVER PRESENTE E NA ORDEM INCORRETA VAI RECEBER AMARELO
            if unidecode(jogador_palavra[indice]) in contador_letras:

                if contador_letras[unidecode(jogador_palavra[indice])] < unidecode(palavra).count(unidecode(jogador_palavra[indice])): # VERIFICA SE A CONTABILIZAÇÃO DA LETRA JÁ ULTRAPASSOU A QUANTIDADE PRESENTE NA PALAVRA CORRETA
                    verificacao[indice] =  f'\033[7;33;40m {jogador_palavra[indice].upper()} \033[m'

                    if unidecode(jogador_palavra[indice]) not in contador_letras:
                            contador_letras[unidecode(jogador_palavra[indice])] = 1
                    else:
                        contador_letras[unidecode(jogador_palavra[indice])] += 1
                else:
                    verificacao[indice] = f'\033[7;37;90m {jogador_palavra[indice].upper()} \033[m'
            else:
                contador_letras[unidecode(jogador_palavra[indice])] = 1
                verificacao[indice] = f'\033[7;33;40m {jogador_palavra[indice].upper()} \033[m'
            if unidecode(jogador_palavra[indice].upper()) not in teclado[0] and unidecode(jogador_palavra[indice].upper()) not in teclado[1]:
                teclado[1].append(unidecode(jogador_palavra[indice].upper()))



    for indice in range(0,len(jogador_palavra)):
        if unidecode(jogador_palavra[indice]) not in unidecode(palavra): # SE A LETRA NÃO ESTIVER PRESENTE NA PALAVRA VAI RECEBER VERMELHO
            verificacao[indice] = f'\033[7;37;90m {jogador_palavra[indice].upper()} \033[m'
            if unidecode(jogador_palavra[indice].upper()) not in teclado[0] and unidecode(jogador_palavra[indice].upper()) not in teclado[1] and unidecode(jogador_palavra[indice].upper()) not in teclado[2]:
                teclado[2].append(unidecode(jogador_palavra[indice].upper()))


    for indice in range(0,len(verificacao)):
        tentativas[tentativas_contador][indice] = verificacao[indice]
    return tentativas







# FUNÇÃO VERIFICA SE O JOGADOR VAI QUERER REINICIAR
def reiniciar():
    deseja_reiniciar = input(print_slow('\nVocê deseja jogar novamente? SIM [s] ou NÂO [n]'))
    while deseja_reiniciar != 's' and deseja_reiniciar != 'n':
            deseja_reiniciar = input(print_slow('Você deseja jogar novamente? SIM [s] ou NÂO [n]'))
    if deseja_reiniciar == 's':
        jogo = True
    else:
        jogo = False
    return jogo










# VERIFICA SE O JOGO CHEGOU AO FIM
def verifica_fim(palavra, jogador_palavra, tentativas_contador, resumo_de_rodadas):
    if unidecode(jogador_palavra) == unidecode(palavra): # VERIFICA SE O JOGADOR ACERTOU A PALAVRA
        print_slow(f'PARABÉNS, VOCÊ ACERTOU A PALAVRA {palavra.upper()}!')
        resumo_de_rodadas[tentativas_contador] += 1
        jogo = False
        resumo_total_rodadas = 0
        for chave in resumo_de_rodadas:
            resumo_total_rodadas += resumo_de_rodadas[chave] # SOMA O TOTAL DE RODADAS PARA TIRAR A PORCENTAGEM PARA O RESUMO
        print_slow(f"\n\nRESUMO DAS ÚLTIMAS PARTIDAS:\nAcertou em uma tentativa: {(resumo_de_rodadas[1]/resumo_total_rodadas)*100:.0f} %\nAcertou em duas tentativas: {(resumo_de_rodadas[2]/resumo_total_rodadas)*100:.0f} %\nAcertou em três tentativas: {(resumo_de_rodadas[3]/resumo_total_rodadas)*100:.0f} %\nAcertou em quatro tentativas: {(resumo_de_rodadas[4]/resumo_total_rodadas)*100:.0f} %\nAcertou em cinco tentativas: {(resumo_de_rodadas[5]/resumo_total_rodadas)*100:.0f} %\nAcertou em seis tentativas: {(resumo_de_rodadas[6]/resumo_total_rodadas)*100:.0f} %\nNão acertou a palavra: {(resumo_de_rodadas['nao_acertou']/resumo_total_rodadas)*100:.0f} %\n\n")
    elif jogador_palavra != palavra and tentativas_contador == 6: # VERIFICA SE AS TENTATIVAS ACABARAM E O JOGADOR NÃO ACERTOU 
        print(f'''
  ___   __   _  _  ____     __   _  _  ____  ____ 
 / __) / _\ ( \/ )(  __)   /  \ / )( \(  __)(  _ \ 
( (_ \/    \/ \/ \ ) _)   (  O )\ \/ / ) _)  )   /
 \___/\_/\_/\_)(_/(____)   \__/  \__/ (____)(__\_)
''')
        print_slow(f'QUE PENA, VOCÊ PERDEU!! A PALAVRA ERA {palavra.upper()}\n')
        resumo_de_rodadas['nao_acertou'] += 1
        jogo = False
        resumo_total_rodadas = 0
        for chave in resumo_de_rodadas:
            resumo_total_rodadas += resumo_de_rodadas[chave]
        print_slow(f"\nRESUMO DAS ÚLTIMAS PARTIDAS:\n\nAcertou em uma tentativa: {(resumo_de_rodadas[1]/resumo_total_rodadas)*100:.0f} %\nAcertou em duas tentativas: {(resumo_de_rodadas[2]/resumo_total_rodadas)*100:.0f} %\nAcertou em três tentativas: {(resumo_de_rodadas[3]/resumo_total_rodadas)*100:.0f} %\nAcertou em quatro tentativas: {(resumo_de_rodadas[4]/resumo_total_rodadas)*100:.0f} %\nAcertou em cinco tentativas: {(resumo_de_rodadas[5]/resumo_total_rodadas)*100:.0f} %\nAcertou em seis tentativas: {(resumo_de_rodadas[6]/resumo_total_rodadas)*100:.0f} %\nNão acertou a palavra: {(resumo_de_rodadas['nao_acertou']/resumo_total_rodadas)*100:.0f} %\n\n")
    else:
        jogo = True
    return jogo



# FUNÇÃO PARA EXIBIR AS LETRAS JÁ USADAS
def exibe_teclado(teclado):
    alfabeto = {'a': '','b': '','c': '','d': '','e': '','f': '','g': '','h': '','i': '','j': '','k': '','l': '','m': '','n': '','o': '','p': '','q': '','r': '','s': '','t': '','u': '','v': '','w': '','x': '','y': '','z': ''}
    for letra in alfabeto:
        if (letra.upper()) in teclado[0]:
            alfabeto[letra] = f'\033[7;32;40m|{teclado[0][teclado[0].index(letra.upper())]}|\033[m'
        elif (letra.upper()) in teclado[1]:
            alfabeto[letra] = f'\033[7;33;40m|{teclado[1][teclado[1].index(letra.upper())]}|\033[m'
        elif (letra.upper()) in teclado[2]:
            alfabeto[letra] = f'\033[7;37;90m|{teclado[2][teclado[2].index(letra.upper())]}|\033[m'
        else:
            alfabeto[letra] = f'|{letra.upper()}|'
    ascii_teclado = f'''
    {alfabeto['q']} {alfabeto['w']} {alfabeto['e']} {alfabeto['r']} {alfabeto['t']} {alfabeto['y']} {alfabeto['u']} {alfabeto['i']} {alfabeto['o']} {alfabeto['p']}

      {alfabeto['a']} {alfabeto['s']} {alfabeto['d']} {alfabeto['f']} {alfabeto['g']} {alfabeto['h']} {alfabeto['j']} {alfabeto['k']} {alfabeto['l']}

          {alfabeto['z']} {alfabeto['x']} {alfabeto['c']} {alfabeto['v']} {alfabeto['b']} {alfabeto['n']} {alfabeto['m']}
'''
    print(ascii_teclado)