from colorama import Fore, Style

#IMPORTANDO DEF's
from perguntas_bitcoin.download_perg import perguntas_ok
from contador_nivel import seleciona_nivel

def main():
    print(Fore.GREEN + ' REGRAS DO JOGO' + Style.RESET_ALL)
    print('Cada pergunta terá quatro respostas alternativas, podendo escolher entre 1, 2, 3 e 4. \n'
    'O jogo termina ao atingir o maior prêmio, desistência ou errar a resposta!')
    print('')
    print('Caro jogador, você pode escolher uma ajuda digitando:')
    print(Fore.YELLOW + ' P ' + Style.RESET_ALL, 'para Pular a pergunta. Neste caso, não avança no prêmio e outra pergunta do mesmo nível é sorteada. Tem direto a usar 3 vezes.')
    print(Fore.RED + ' D ' + Style.RESET_ALL,'para Desistir da partida. Neste caso, o você recebe metade do prêmio conquistado e a partida é encerrada.')
    print('Caso erre a resposta, ganhará 10% do valor conquistado até o momento.')
    print('')
    
    # VERIFICA AS REPOSTAS DO USÁRIO
    resultado, premio = seleciona_nivel(letra=None, premio=0)

    # AO RETORNAR D O USUÁRIO GANHA 50% DO PRÊMIO TOTAL
    if resultado == 'd':
        valor_premio = premio * 0.50
        print('')
        print(f'Prêmio conquistado foi de {valor_premio:.2f}BTC (/^▽^)/')
        print('')

    # AO RETORNAR E O USUÁRIO GANHA 10% DO PRÊMIO TOTAL
    elif resultado == 'e':
        valor_premio = premio * 0.10
        print('')
        print(f'Prêmio conquistado foi de {valor_premio:.2f}BTC (/^▽^)/')
        print('')

    # AO NÃO RETORNAR NENHUMA LETRA OU SEJA A PADRÃO NONE, O USUÁRIO ACERTOU TODAS AS PERGUNTAS E GANHO O PRÊMIO MÁXIMO
    else:
        print(f'Parabéns, você ganhou o prêmio máximo de {premio:.0f}BTC')
        print('')
        print(Fore.GREEN + '(/^▽^)/  （⌒▽⌒) ゞ   (/•ิ_•ิ)/ ' + Style.RESET_ALL)
        print('')

# VERIFICA A CONEXÃO COM  INTERNET ANTES DE INICIAR O JOGO
perguntas = perguntas_ok()
if perguntas == True:
    main()
else:
    print('Falha na conexão. Verifique a internet e tente novamente.')
    print('')