# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salário = float(input('Qual o salário do funcionário? R$ '))
novo = salário + (salário * 15 / 100)
print(f'O novo salário do funcionário com o aumento de 15% é de R$ {novo:.2f}')