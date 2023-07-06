"""
Programa que lê a altura e largura de uma parede<calcula sua área quadrada e
faz o calculo da quantidade de tinta que precisará para pintá-la.
"""
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
media_tinta = float(input('Informe a quantidade de tinta necessária para cada m²: '))
tinta_gasta = area / media_tinta
print(f'A parede informada de {altura} x {largura} possue uma área de: {area:.2f}mts².')
print(f'Para pintar essa área precisaremos de {tinta_gasta:.2f}lts.')
