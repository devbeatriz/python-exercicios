# Escreva um programa que leia um valor em metros e exiba convetido em centímetros a milímetros
medida = float(input('Uma distância em metros: '))
print(f'{medida/1000}km \n{medida/100}hm \n{medida/10}dam\n{medida*10:.0f}dm\n{medida*100:.0f}cm\n{medida*1000:.0f}mm')
