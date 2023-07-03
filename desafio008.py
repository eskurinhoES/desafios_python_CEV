#Programa que lê uma medida em metros e mostra essa medida em
#em centímetros e milímetros
medida = float(input('Digite a medida em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}mts corresponde a: ')
print(f'{cm:.2f} centímetros.')
print(f'{mm:.2f} milímetros.')
