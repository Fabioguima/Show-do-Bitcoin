#IMPORTANDO DEF's
from perguntas_bitcoin.ran_perguntas import escolher_e_remover_pergunta
from resposta_user import jogar_perguntas

def seleciona_nivel(letra : str, premio : float)-> tuple:

    # CONTADOR DE NIVEIS
    contador_easy = 0
    contador_medium = 0
    contador_hard = 0

    # SOMATÓRIO DO PRÊMIO
    premio = 0

    # VERIFICA A QUANTIDADE DE VEZES JA PASSOU PELO NIVEL EASY
    while contador_easy < 3:
        pergunta, resposta_certa, resposta_errada = escolher_e_remover_pergunta('Show_do_bitcoin/perguntas_bitcoin/perguntas_easy.json')
        letra = jogar_perguntas(pergunta, resposta_certa, resposta_errada)

        # COMPARA ENTRE A LETRA A, D, E PARA VERIFICAR O ACERTO, DESISTÊNCIA OU ERRO
        if letra == 'a':
            contador_easy += 1
            premio += 0.1
            print('')
            print(f'Prêmio até aqui {premio:.1f}BTC')
            print('')
            print(f'Caso desista seu PRÊMIO será {premio * 0.50:.2f}BTC, se errar {premio * 0.10:.2f}BTC')
            print('')
        if letra == 'd': return 'd', premio
        if letra == 'e': return 'e', premio

    # VERIFICA A QUANTIDADE DE VEZES JA PASSOU PELO NIVEL MEDIUM
    while contador_medium < 3:
        pergunta, resposta_certa, resposta_errada = escolher_e_remover_pergunta('Show_do_bitcoin/perguntas_bitcoin/perguntas_medium.json')
        letra = jogar_perguntas(pergunta, resposta_certa, resposta_errada)

        # COMPARA ENTRE A LETRA A, D, E PARA VERIFICAR O ACERTO, DESISTÊNCIA OU ERRO
        if letra == 'a':
            contador_medium += 1
            premio += 0.1
            print('')
            print(f'Prêmio até aqui {premio:.1f}BTC')
            print('')
            print(f'Caso desista seu PRÊMIO será {premio * 0.50:.2f}BTC, se errar {premio * 0.10:.2f}BTC')
            print('')
        if letra == 'd': return 'd', premio
        if letra == 'e': return 'e', premio

    # VERIFICA A QUANTIDADE DE VEZES JA PASSOU PELO NIVEL HARD
    while contador_hard < 4:
        pergunta, resposta_certa, resposta_errada = escolher_e_remover_pergunta('Show_do_bitcoin/perguntas_bitcoin/perguntas_hard.json')
        letra = jogar_perguntas(pergunta, resposta_certa, resposta_errada)

        # COMPARA ENTRE A LETRA A, D, E PARA VERIFICAR O ACERTO, DESISTÊNCIA OU ERRO
        if letra == 'a':
            contador_hard += 1
            premio += 0.1
            print('')
            print(f'Prêmio até aqui {premio:.1f}BTC')
            print('')
            print(f'Caso desista seu PRÊMIO será {premio * 0.50:.2f}BTC, se errar {premio * 0.10:.2f}BTC')
            print('')
        if letra == 'd': return 'd', premio
        if letra == 'e': return 'e', premio

    # RETORNA QUANDO SE ACERTA AS 10 PERGUNTAS DANDO ASSIM O PRÊMIO TOTAL
    return letra, premio

