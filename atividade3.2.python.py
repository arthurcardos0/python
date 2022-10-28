#Crie um programa para realizar as operações de uma tabuada de multiplicação, onde será solicitado ao usuário digitar qual
#numero será a tabuada e qual intervalo do inicio e fim da
#tabuada, e exibir na tela o resultado conforme intervalo.

print ("tabuada")

numero = int(input("Qual número você deseja saber a tabuda? "))
inicio = int(input("Digite o inicio do intervalo da tabuada: "))
fim = int(input("Digite o fim do intervalo da tabuda: "))

print("Tabuada de ", numero, "de ", inicio, "até ", fim)
for i in range(inicio,fim):
    print(numero, "*", 1, "=", (numnero*(1)))
