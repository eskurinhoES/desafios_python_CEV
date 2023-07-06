"""
Programa que lê a temperatura em graús celsius e transforma
em graús farenheit
"""
c = float(input('Digite a temperatura em °C: '))
f = 9 * c / 5 + 32
print(f'A temperatura {c:.1f}°C, corresponde à {f:.1f}°F .')
