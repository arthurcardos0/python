#Faça um Programa que leia em um vetor de 10 caracteres (letras ) e diga quantas consoantes foram lidas.
#Mostre as consoantes.

vetor = string[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0]]

for i in range(5):
    for j in range(5):
        vetor [i, j] = string("Digite algumas letras sem ser a, e, i, o ,u: "))

n1 = string(input("Digite uma letra sem ser a, e, i, o ,u: "))
encontrado = False

for i in range(5):
    for j in range(5):
        if vetor [i, j] == n1:
            print("Letra encontrada: ", n1, "na posição ", vetor, i, j)
            enconttrado = True

if encontrado is False:
    print("Não foi encontrado na busca sua(s) letra(s).")

print(vetor)

