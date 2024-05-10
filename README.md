# Analise_de_sentimento_Python

Olá pessoal! Quero compartilhar com vocês um projeto bem simples e prático de aprendizado de máquina em Python que desenvolvi durante o Santander Bootcamp 2024 com o auxilio do time da DIO. 

O projeto é bem simples para praticarmos os conceitos e começar a formular a ideia de como funciona um algoritmo de Aprendizado de Maquina.
Ele consiste em treinar um algoritmo para receber comentários, ler e identificar se o sentimento do comentário é positivo, negativo ou neutro e retornar o resultado dessa análise utilizando Python.

Criei basicamente 3 funções para isso que consistem em:

1. Receber o comentário de usuários e definir se é um comentário válido.

2. Dividi o comentário em palavras, removendo pontuações e caracteres especiais, através da função "re.findall()" do módulo "re" que fornece operações para trabalhar com expressões regulares.

3. Criei 3 variáveis no formato de listas que considero palavras "positivas", "negativas" e "neutras". 
Fiz a análise das palavras e a contagem baseada nessas variáveis.
Por ultimo usei a condicional if para analisar a quantidade de palavras e definir se há mais palavras positivas, negativas ou neutras no comentário retornando então o resultado da análise de sentimento.

Assista para entender como foi projetado, como funciona e como adaptei o projeto com novas ideias!
