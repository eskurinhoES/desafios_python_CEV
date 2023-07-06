"""
Programa que lê o nome do usuário e informa se existe a
palavra 'Silva' no nome informado
"""
nome = str(input('Digite seu nome completo: ')).strip()
if 'silva' in nome.lower():
    print('Seu nome possue a palavra "Silva".')
else:
    print('Seu nome não possue a palavra "Silva"')
