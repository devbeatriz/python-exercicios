# Faça um algoritmo que leia o preço de um produto e mostre seu preço, com 5% de desconto
preço = float(input('Qual é o preço do produto? R$ '))
desconto = preço - (preço *5 / 100)
print(f'O valor do produto com 5% de desconto é de R$ {desconto:.2f}')