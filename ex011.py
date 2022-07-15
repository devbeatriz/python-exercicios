# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura * altura 
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {área}m²')
tinta = área / 2
print(f'Para pintar essa parede, você precisará de {tinta} litros de tinta')