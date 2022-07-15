# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar. Considere U$ 1,00 = R$ 3,27

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.40
print(f'Com {real} você pode comprar U$ {dolar:.2f}')