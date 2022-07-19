# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1 - O nomes com todas as letras maiúsculas
# 2 - O nome com todas as letras minusculas
# 3 -Quantas letras ao todo (sem considerar espaços)
# 4 - Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculo é {(nome.upper())}')
print(f'Seu nome em minusculo é {(nome.lower())}')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(len((nome.split())[0])))