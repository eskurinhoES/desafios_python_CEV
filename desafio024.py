"""
Programa que lê a cidade onde o usuário nasceu e verifica se existe
a palavra 'Santo' no início.
"""
cidade = str(input('Digite a cidade onde nasceu: ')).strip()
print(f'Analisando a cidade informada: {cidade.upper()}.')
if cidade[:5].upper() == 'SANTO':
    print('A cidade que você mora tem a palavra "SANTO" no início.')
else:
    print('A cidade que você mora não tem a palavra "SANTO" no início.')
