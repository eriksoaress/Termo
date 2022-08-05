from time import sleep
import os
from unidecode import unidecode
from funcoes import sorteia_palavra,valida_palavra, verifica_letras, verifica_fim, reiniciar, exibe_teclado, print_slow
from palavras import palavras

jogo = True
acertou = False
resumo_de_rodadas = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 'nao_acertou': 0}
while jogo == True:
    # COMANDO PUBLICADO POR MATHEUS BATTISTI (https://www.horadecodar.com.br/2020/04/24/como-limpar-o-console-no-python-terminal/)
    os.system('cls' if os.name == 'nt' else 'clear') # LIMPA A TELA
    teclado = [[],[],[]]
    acertou = False
    tentativas_contador = 0
    # ARMAZENA AS LETRAS DE CADA TENTATIVA
    tentativas = [['   ','   ','   ','   ','   '],['   ','   ','   ','   ','   '],['   ','   ','   ','   ','   '],['   ','   ','   ','   ','   '],['   ','   ','   ','   ','   '],['   ','   ','   ','   ','   ']]
    comecar = input(print_slow('\nPressione a tecla ENTER para iniciar o jogo: '))
    while comecar != '':
        comecar = input(print_slow('Pressione a tecla ENTER para iniciar o jogo: '))
    sleep(0.3)
    print('''
 ____  ____  _  _    _  _  __  __ _  ____   __  
(  _ \(  __)( \/ )  / )( \(  )(  ( \(    \ /  \ 
 ) _ ( ) _) / \/ \  \ \/ / )( /    / ) D ((  O )
(____/(____)\_)(_/   \__/ (__)\_)__)(____/ \__/ 
''')
    print_slow('\nVocê precisa acertar a palavra em até 6 tentativas.\n\nAqui vão algumas dicas para te auxiliar:\n\n\033[7;32;40m   \033[m significa que a letra está presente na palavra e na posição correta.\n\n\033[7;33;40m   \033[m significa que a letra está presente na palavra, mas está na posição errada.\n\n\033[7;37;90m   \033[m significa que a letra não está presente na palavra.\n\n')
    sleep(0.5)
    palavras_lista = palavras()
    palavra = sorteia_palavra(palavras_lista)
    while jogo == True and tentativas_contador != 6 and acertou == False: #SÓ CONTINUA AS NOVAS RODADAS ENQUANTO AS TENTAIVAS NÃO SE ESGOTAREM E O JOGADOR NÃO ACERTAR A PALAVRA
        if tentativas_contador > 0:
            exibe_teclado(teclado)
        jogador_palavra = valida_palavra(palavras_lista, tentativas_contador)
        os.system('cls' if os.name == 'nt' else 'clear')
        verificacao = verifica_letras(palavra, jogador_palavra, tentativas_contador, tentativas, teclado)
        verificacao_rodada = ''
        template = f'''
1º |{tentativas[0][0]}| |{tentativas[0][1]}| |{tentativas[0][2]}| |{tentativas[0][3]}| |{tentativas[0][4]}|

2º |{tentativas[1][0]}| |{tentativas[1][1]}| |{tentativas[1][2]}| |{tentativas[1][3]}| |{tentativas[1][4]}|

3º |{tentativas[2][0]}| |{tentativas[2][1]}| |{tentativas[2][2]}| |{tentativas[2][3]}| |{tentativas[2][4]}|

4º |{tentativas[3][0]}| |{tentativas[3][1]}| |{tentativas[3][2]}| |{tentativas[3][3]}| |{tentativas[3][4]}|

5º |{tentativas[4][0]}| |{tentativas[4][1]}| |{tentativas[4][2]}| |{tentativas[4][3]}| |{tentativas[4][4]}|

6º |{tentativas[5][0]}| |{tentativas[5][1]}| |{tentativas[5][2]}| |{tentativas[5][3]}| |{tentativas[5][4]}|
'''
        print(f'\n              RODADA {tentativas_contador + 1}\n {template}')
        tentativas_contador += 1
        jogo = verifica_fim(palavra, jogador_palavra, tentativas_contador, resumo_de_rodadas)
        if unidecode(jogador_palavra) == unidecode(palavra):
            acertou = True
        if jogo == False:
            jogo = reiniciar()