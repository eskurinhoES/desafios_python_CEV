"""
Programa que lê o nome de 6 alunos e escolhe a ordem
de apresentação dos trabalhos em sala de aula
"""
from random import shuffle
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
n5 = str(input('Digite o nome do quinto aluno: '))
n6 = str(input('Digite o nome do sexto aluno: '))
lista = [n1, n2, n3, n4, n5, n6]
print(f'A lista de alunos digitada foi essa:')
print(lista)
print(f'E a ordem de apresentação dos trabalhos ficou assim: ')
shuffle(lista)
print(lista)
