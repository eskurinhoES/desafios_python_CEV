"""
Programa que lê o salário de um funcionário e mostra seu novo
salário com 15% de aumento.
"""
salario = float(input('Digite o salário do funcionário: R$ '))
aumento_real = salario * 15 / 100
salario_novo = salario + aumento_real
print(f'O funcionário que ganhava R$ {salario:.2f}')
print(f'Recebeu um aumento de 15% num total de R$ {aumento_real:.2f}')
print(f'E passou a receber um salário de R$ {salario_novo:.2f} .')
