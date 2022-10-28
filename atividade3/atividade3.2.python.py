#Crie um programa para realizar as operações de uma tabuada de multiplicação, onde será solicitado ao usuário digitar qual
#numero será a tabuada e qual intervalo do inicio e fim da
#tabuada, e exibir na tela o resultado conforme intervalo.

print ("Tabuada do número desejado")

tabuada = int(input("Digite o número da tabuada: "))
inicio = int(input("Digite o início do intervalo da tabuada: "))
fim = int(input("Digite o fim do intervalo da tabuda: "))

for i in range(inicio, fim + 1):
    print("Tabuada do número", tabuada, " resultado ", tabuada, "*", inicio, "=", tabuada * inicio)
    print("Tabuada resultado: ", tabuada * inicio)
    inicio = inicio + 1
