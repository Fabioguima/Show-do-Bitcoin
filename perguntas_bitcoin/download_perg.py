import requests
import json

def get_token():
    try:
        response = requests.get('https://tryvia.ptr.red/api_token.php?command=request', timeout=10)

        # VERIFICA SE A REQUISIÇÃO FOI BEM-SUCEDIDA
        response.raise_for_status()
        data = response.json()
        if data.get('response_code') == 0:
            return data['token']
        else:
            print('Erro ao obter token:')

     # ERRO DE CONEXÃO AO OBTER O TOKEN
    except:
        print('')


def get_questions(token, qtd_questions, difficulty):
    category = 0  # Você pode mudar a categoria se desejar
    url = (
        f'https://tryvia.ptr.red/api.php'
        f'?amount={qtd_questions}'
        f'&category={category}'
        f'&type=multiple'
        f'&difficulty={difficulty}'
        f'&token={token}'
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get('response_code') == 0:
            return data['results']
    return []

def salvar_perguntas_em_pastas(token):
    perguntas_easy = get_questions(token, 6, 'easy')
    perguntas_medium = get_questions(token, 6, 'medium') # PERGUNTAS DE DIFERENTES DIFICULDADES
    perguntas_hard = get_questions(token, 7, 'hard')

    # SALVAR PERGUNTAS EM ARQUIVOS SEPARADOS
    with open('Show_do_bitcoin/perguntas_bitcoin/perguntas_easy.json', 'w', encoding='utf-8') as arquivo:
        json.dump(perguntas_easy, arquivo, ensure_ascii=False, indent=4)

    with open('Show_do_bitcoin/perguntas_bitcoin/perguntas_medium.json', 'w', encoding='utf-8') as arquivo:
        json.dump(perguntas_medium, arquivo, ensure_ascii=False, indent=4)

    with open('Show_do_bitcoin/perguntas_bitcoin/perguntas_hard.json', 'w', encoding='utf-8') as arquivo:
        json.dump(perguntas_hard, arquivo, ensure_ascii=False, indent=4)

def perguntas_ok():
    arquivos_e_perguntas = [
        ('Show_do_bitcoin/perguntas_bitcoin/perguntas_easy.json'),
        ('Show_do_bitcoin/perguntas_bitcoin/perguntas_medium.json'),
        ('Show_do_bitcoin/perguntas_bitcoin/perguntas_hard.json'),
    ]
    
    # VERIFICA SE AS PERGUNTAS DE CADA ARQUIVO FOI FEITO O DOWNLOAD CORRETO OU SEJA SE NÃO ESTA COM A LISTA VAZIA
    for perguntas in arquivos_e_perguntas:
        with open(perguntas, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            if dados == []:

                # CASO ESTEJA FAZIA RETORNA FALSE E O JOGO NÃO INICIA
                return False
    return True


# Executar o processo
token_atual = get_token()
if token_atual:
    salvar_perguntas_em_pastas(token_atual)

    
    