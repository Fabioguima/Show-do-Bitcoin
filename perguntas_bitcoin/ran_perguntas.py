import json
import random

def escolher_e_remover_pergunta(caminho_arquivo : str)-> list:

    #ABRE O ARQUIVO .JSON
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        perguntas = json.load(arquivo)
    
    #ESCOLHE PERGUNTA ALEATORIA
    pergunta_escolhida = random.choice(perguntas) 
    
    pergunta = pergunta_escolhida["question"]
    resposta_certa = pergunta_escolhida["correct_answer"]
    resposta_errada = pergunta_escolhida["incorrect_answers"]

    # REMOVE A PERGUNTA ESCOLHIDA PARA QUE NÃO SE REPITA
    perguntas.remove(pergunta_escolhida)
    
    # SALVA A LISTA ATUALIZADA
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo: 
        json.dump(perguntas, arquivo, ensure_ascii=False, indent=4)

    return pergunta, resposta_certa, resposta_errada