from colorama import Fore, Style
import random

pulos_disponiveis = 3

def jogar_perguntas(pergunta : str, resposta_certa : str, resposta_errada : str)-> str:
    global pulos_disponiveis
    pergunta_maiuscula = pergunta.upper()

    # LAÇO VERIFICAÇÃO RESPOSTA DO USUÁRIO É VALIDA
    for perguntas in pergunta:

        # EMBARALHAR OPÇÕES DE RESPOSTA
        opcoes = resposta_errada + [resposta_certa]
        random.shuffle(opcoes)

        # MOSTRA PERGUNTA
        print(Fore.GREEN + pergunta_maiuscula + Style.RESET_ALL)
        # MOSTRA RESPOSTA E AS ENUMERA
        for enumeracao, opcao in enumerate(opcoes, 1):
            print(f"{enumeracao}. {opcao}")

        # VERIFICA SE TEM PULOS DISPONIVEIS
        if pulos_disponiveis > 0:
            print(f"Você pode pular esta pergunta. Pulos restante: {pulos_disponiveis}")
            resposta_usuario = input(f'Seu palpite ou{Fore.YELLOW} P {Style.RESET_ALL}-> pular, {Fore.RED} D {Style.RESET_ALL}-> desistir: ').strip()
        else:
            resposta_usuario = input(f"Digite o número da sua resposta ou{Fore.RED} D {Style.RESET_ALL}-> desistir:  ").strip()

        # VERIFICA SE A RESPOSTA DO USUÁRIO FOI P PARA ASSIM PULAR A PERGUNTA PARA UMA DE MESMO NIVEL
        if resposta_usuario.lower() == 'p':
            if pulos_disponiveis > 0:
                pulos_disponiveis -= 1
                print('')
                print("Pergunta pulada! Vamos para a próxima.")
                print('')
                return 'p'
            else:
                print('')
                print("Você não tem mais pulos disponíveis. Responda a pergunta.")
                print('')
                resposta_usuario = input(f"Digite o número da sua resposta{Fore.RED} D {Style.RESET_ALL}-> desistir:  ").strip()

        # VERIFICA SE A RESPOSTA DO USUÁRIO FOI D, ASSIM LEVANDO A DESISTÊNCIA DO GAME
        if resposta_usuario.lower() == 'd':
            return 'd'

        # VERIFICA SE A RESPOSTA DADA EM NUMEROS ESTÁ CORRETA
        try:
            resposta_numero = int(resposta_usuario)

            # VERIFICA SE A RESPOSTA DO USUÁRIO ESTA ENTRE O INTERVALO DE RESPOSTA 
            if 1 <= resposta_numero <= len(opcoes):

                # SUBTAI -1 DO INDICE PARA PEGAR A POSIÇÃO CORRETA NA LISTA DE OPÇÕES
                resposta_escolhida = opcoes[resposta_numero - 1]

                # VERIFICA A RESPOSTA RECEBIDA COM A REPOSTA CERTA
                if resposta_escolhida == resposta_certa:
                    print("Parabéns! Você acertou.")
                    return 'a'
                else:
                    print('')
                    print(f"Que pena! Você errou. A resposta correta era: {resposta_certa}")
                    print('')
                    return 'e'
            else:
                print('')
            print(f"Tente Novamente. Respostas válidas (1, 2, 3, 4,{Fore.YELLOW} P{Style.RESET_ALL} ou {Fore.RED}D{Style.RESET_ALL})") # RESPOSTA VÁLIDA NUMEROS
            print('')
            continue
        except:
            print('')
            print(f"Tente Novamente. Respostas válidas (1, 2, 3, 4 ou {Fore.RED}D{Style.RESET_ALL})") # RESPOSTA VÁLIDA LETRAS
            print('')
            continue