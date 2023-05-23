'''
Exibir todos os numeros existentes na sequencia de 1 a 500
'''

contador = 1

while ( contador < 20):
    print( contador )
    contador = contador + 1
    if ( contador == 10 ):
        print("### INICIO DO BLOCO DO IF ###")
        print("Neste momento o contador vale 10")
        continue # Volta para o While a partir daqui
        print("### FIM DO BLOCO DO IF ###")
print("--- Linha apos o bloco do while ---")
print("### FIM DO PROGRAMA ###")

