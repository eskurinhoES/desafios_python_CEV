"""
Programa que lê a quantidade de dias alugados por um carro e quantos
kms foram rodados. O retorno do programa é o valor a ser pago,considerando o
valor de R$ 60.00 o valor da diária e R$ 0.15 o km rodado.
"""
valor_km_rodado = 0.15
diaria = 60
dias = int(input('Informe os dias alugados: '))
kms_rodados = float(input('Informe os kms rodados: '))
total_diarias = dias * diaria
print(f'Foram alugados {dias} dias e o valor das diárias ficou em R$ {total_diarias:.2f}')
total_em_kms_rodados = kms_rodados * valor_km_rodado
print(f'Foram rodados {kms_rodados}kms e o total ficou em R$ {total_em_kms_rodados:.2f} ')
total_a_pagar = total_diarias + total_em_kms_rodados
print(f'E o total a pagar pelo aluguel do veículo ficou R$ {total_a_pagar:.2f}!')
