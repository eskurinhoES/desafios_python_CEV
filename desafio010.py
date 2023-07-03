#Programa que converte o valor em reais informado pelo usuário e
#converte para dólar
cotacao = 3.27
reais = float(input('Digite o valor que deseja converter: R$ '))
dolares = reais / cotacao
print(f'Reais informados R$ {reais} .')
print(f'Considerando a cotação,você vai receber $ {dolares:.2f} .')
