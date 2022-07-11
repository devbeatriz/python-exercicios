# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
num = int(input('Digite um número para ver sua tabuada; '))
c = 0
print(f'A tabuada é {num}: ')
while(c <= 10):
    print(f'{num} x {c} = {num*c}')
    c = c+1
