# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não ocm o nome "SANTO"
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')