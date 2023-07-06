"""
Programa que lê o preço de um produto e calcula seu novo preço
com 5% de desconto
"""
preco = float(input('Digite o preço do produto: R$ '))
novo_preco = preco - (preco * 5 / 100)
print(f'O desconto total do produto com 5% é de: R$ {preco * 5 / 100:.2f}')
print(f'O produto que custava R$ {preco:.2f},passará a custar R${novo_preco:.2f}')
print('com os 5% de desconto.')
