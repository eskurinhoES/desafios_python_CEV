"""
Programa que lê uma frase qualquer digitada pelo usuário,informa quantas
vezes aparece a letra 'A',qual a posição da primeira e última ocorrência da letra
'A' na frase
"""
frase = str(input('Digite a frase a ser analisada: ')).upper().strip()
print(f'A letra "A" aparece {frase.count("A")} vezes na frase.')
print(f'A primeira vez que aparece a letra "A" é na posição {frase.find("A") + 1}')
print(f'E a última vez uqe aparece a letra "A" é na posição {frase.rfind("A") + 1}')
