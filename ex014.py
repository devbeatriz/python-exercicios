# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. #
from math import trunc
num = float(input('Digite um valor: '))
print(f'A porção inteira do valor {num} é {trunc(num)}.')