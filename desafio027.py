nome = str(input('Digite seu nome completo: ')).strip()
print(f'Muito prazer em te conhecer {nome}!')
n = nome.split()
primeiro = n[0]
ultimo = n[len(n) - 1]
print(f'Seu primeiro nome é {primeiro}.')
print(f'Seu último nome é {ultimo}.')
