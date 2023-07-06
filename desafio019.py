"""
Programa que lê o nome de 5 alunos e sorteia um deles
para apagar o quadro negro.
"""
from random import choice
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
aluno5 = str(input('Digite o nome do quinto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
escolhido = choice(lista)
print(f'O aluno escolhido para apagar o quadro negro foi: {escolhido}!')
