# Faça um programa que leia um nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')