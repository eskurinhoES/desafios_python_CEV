"""
Programa que lê o cateto oposto,cateto adjacente e mostra a hipotenusa
desse triângulo retângulo
"""
from math import hypot


co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa desse triângulo retângulo é: {hi:.2f}')
