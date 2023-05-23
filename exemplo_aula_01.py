'''
Perguntar nome, idade e salário da pessoa;
Em seguida exibir estes dados
'''

# Comentário de 1 linha

nome = input("Qual seu nome? ")
print(f"Olá {nome}, tudo bem?")
#print("var nome: ", type(nome))

idade = int(input("Qual é a sua idade? "))
print(f"Nossa! você tem apenas {idade}? Nem parece.")
#print("var idade: ", type(idade))

salario = float(input("Qual salário pretendido? "))
print(f"O salário de {salario:.2f} é interessante.")
#print("var salário: ", type(salario))

