'''
Questao 5 da lista 5.1
Desenvolver um programa que apresente os resultados de uma tabela de um numero qualquer.
Ela deve ser impressa no seguinte formato:
Considerando como exemplo o fornecimento do numero 2
2.1=2
2.2=4
2.3=6...
'''

numero = int(input("Digite um numero"))
i = 1
while ( i <= 10):
    print(f"{numero} x {i} = {i * numero}")
    i = i + 1


