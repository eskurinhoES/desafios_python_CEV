"""
Programa que lê um ângulo qualquer e calcula o seno, coseno e
tangente desse ângulo
"""
from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
print(f'O seno do ângulo {angulo}° é {seno:.2f}')
coseno = cos(radians(angulo))
print(f'O coseno do ângulo {angulo}° é {coseno:.2f}')
tangente = tan(radians(angulo))
print(f'A tangente do ângulo {angulo}° é {tangente:.2f}')
