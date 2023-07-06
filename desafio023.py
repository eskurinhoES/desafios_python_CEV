"""
Programa que lê um número de 0 a 9999 e mostra na tela sua unidade, dezena,
centena e milhar separadamente.
"""
num = int(input('Digite um número inteiro de 0 a 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f'Analisando o número: {num}')
print(f'Unidade : {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
