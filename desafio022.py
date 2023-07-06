"""
Programa que faz a análise de um nome completo informando como fica o nome com
todas as letras maiúsculas,todas minúsculas,quantas letras possue o nome sem
considerar espaços e quantas letras possue o primeiro nome.
"""
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('Ele com todas as letras maiúsculas fica: ')
print(f'{nome.upper()}')
print('Ele com todas as letras minúsculas fica: ')
print(f'{nome.lower()}')
print(f'Seu nome tem ao total {len(nome) - nome.count(" ")}')
#print(f'Seu primeiro nome tem {nome.find(" ")} letras.')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele possue {len(separa[0])} letras.')
