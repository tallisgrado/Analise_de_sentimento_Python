import re
from collections import Counter

def obter_comentario():
    while True:
        comentario = input("Por favor, insira seu comentário a respeito do atendimento recebido: ").strip()
        if comentario:
            return comentario
        else:
            print("Por favor, insira um comentário válido.")

def dividir_comentario_em_palavras(comentario):
    return re.findall(r'\b\w+\b', comentario.lower())
    
def analisar_sentimento(comentario):

    positivas = ["bom", "boa", "ótimo", "excelente", "maravilhoso", "gostei", "incrível","fantástico","sim"]
    negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio","decepção","não","demorou"]
    neutras = ["mas", "deixou", "apesar", "embora"]

    palavras = dividir_comentario_em_palavras(comentario)
    contagem_palavras = Counter(palavras)

    count_positivo = sum(palavra in positivas for palavra in palavras)
    count_negativo = sum(palavra in negativas for palavra in palavras)
    count_neutro = sum(palavra in neutras for palavra in palavras)

    if count_positivo > count_negativo and count_neutro == 0:
        return "Positivo"
    elif count_negativo > count_positivo and count_neutro == 0:
        return "Negativo"
    else:
        return "Neutro"

comentario = obter_comentario()
sentimento = analisar_sentimento(comentario)
print("O atendimento foi:", sentimento)