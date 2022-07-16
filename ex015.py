# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retãngulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Comprimeto do cateto oposto: '))
ca = float(input('Comprimeto do cateto adjacente: '))
hi = hypot(co,ca)
print (f'A hipotenusa vai medir {hi:.2f}')
