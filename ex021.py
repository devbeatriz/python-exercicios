# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digitire um número: 1834 | Unidade: 4 Dezena: 3 Centena:8 Milhar:1
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número: {num}\n Unidade: {u}\n Dezena: {d}\n Centena: {c}\n Milhar: {m}')
