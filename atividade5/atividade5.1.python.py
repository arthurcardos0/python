#Faça um Programa que leia em um vetor de 10 caracteres (letras ) e diga quantas consoantes foram lidas.
#Mostre as consoantes.

print("Programa para mostrar consoantes")
vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    vetor[i] = input("Digite uma letra: " + str(i) + ": " )
print(vetor)

contador = 0

for i in range(10):
    if not (vetor[i] == str("a") or vetor[i] == str("e") or vetor[i] == str("i") or vetor[i] == str("o") or vetor[1] == str("u")):
         print("Consoante ma posição: " + str(i+1) + ": ", vetor[i])
         contador = contador + 1

print("O número total de consoantes é: ", contador)

