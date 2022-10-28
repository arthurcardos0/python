# Igual, maior, menor que 10

print ("Programa adivinha número inteir")
num1 = int(input("Digite um número inteiro: "))
#não será tratado erro de digitação do úsuario
if num1 > 10:
    print ("O número " + str(num1) + " digitado é maior que o número secreto")
elif num1 < 10:
    print ("O número ", num1, " digitado é menor que o número secreto")
else:
    print (num1, "Acertou o número secreto!")
