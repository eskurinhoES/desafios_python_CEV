#Programa que lê duas notas de um aluno e imprime a sua média
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'As notas do aluno foram:')
print(f'Nota 1: {nota1}')
print(f'Nota 2: {nota2}')
print(f'A média do aluno foi: {media:.2f}')
