'''
Crie um programa que pergunte um numero ao usuario
Em seguida o programa deve informar se o numero inserido
- esta abaixo fde 100
- entre 100 e 200
- acima de 200
'''

num = int(input("Informe um Numero"))

if (num < 100 ):
    print(f"{num} está abaixo de 100")
else:
    if (num <= 200 ):
        print(f"{num} esta entre 100 e 200")
    else:
        print(f"{num} esta acima de 200")