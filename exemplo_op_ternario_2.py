'''
Crie um programa que pergunte a idade do usario e em sequida informe se
este usuario e menor de idade ou maior de idade.
'''

idade = int(input("Informe a sua idade: "))

resposta = "maior de idade" if idade >= 18 else "menor de idade"

print(f"Você é {resposta}")
