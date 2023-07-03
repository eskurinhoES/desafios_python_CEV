#Programa que lê algo pelo teclado,mostra seu tipo primitivo e todas
#informaçẽs possíveis sobre ele.
algo = input('Digite algo: ')
print(f'O tipo primitivo de {algo} é: {type(algo)}')
print(f'{algo} é numérico? {algo.isnumeric()}')
print(f'{algo} é alfanumérico? {algo.isalnum()}')
print(f'{algo} tem somente espaços? {algo.isspace()}')
print(f'{algo} é alfabético? {algo.isalpha()}')
print(f'{algo} está em letras minúsculas? {algo.islower()}')
print(f'{algo} está em letras maiúsculas? {algo.isupper()}')
print(f'{algo} está capitalizada? {algo.istitle()}')
