'''
Crie um programa que pergunte a idade do usario e em sequida informe se
este usuario e menor de idade ou maior de idade.
'''

idade = int(input("Informe a sua idade: "))

resposta = ("menor de idade", "maior de idade") [idade >= 18]

print(f"Você é {resposta}")
