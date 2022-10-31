#Crie um programa para calcular as notas obtidas pelo aluno do ensino médio, deverá mostrar mensagem para ser digitado a
#nota da 1ª, 2ª, 3ª e 4ª prova e a nota do 1º, 2º, 3º e 4º trabalho.
#Após deverá mostrar na tela a média obtida no 1º, 2º, 3º e 4º bimestre.
#E depois o total informado se o aluno foi aprovado, esta em
#recuperação ou foi reprovado sem recuperação.

print("Programa para calcular as notas de provas e trabalhos")

print("Digite suas notas referente as provas e trabalhos.")
print("Notas das provas vão de 0 a 12.5!")
print("Notas dos trabalhos vão de 12.5!")
prova1 = float(input("Valor da nota referente a primeira prova: "))
prova2 = float(input("Valor da nota referente a segunda prova: "))
prova3 = float(input("Valor da nota referente a terceira prova: "))
prova4 = float(input("Valor da nota referente a quarta prova: "))
resultado_provas = prova1 + prova2 + prova3 + prova4
print("Valor da somatoria das notas das provas é: ", resultado_provas)
trabalho1 = float(input("Valor da nota referente ao primeiro trabalho: "))
trabalho2 = float(input("Valor da nota referente ao segundo trabalho: "))
trabalho3 = float(input("Valor da nota referente ao terceiro trabalho: "))
trabalho4 = float(input("Valor da nota referente ao quarto trabalho: "))
resultado_trabalhos = trabalho1 + trabalho2 + trabalho3 + trabalho4
print("Valor da somatoria das notas dos trabalhos é: ", resultado_trabalhos)
media1 = prova1 + trabalho1
print("Valor da media do primeiro bimestre é: ", media1)
media2 = prova2 + trabalho2
print("Valor da media do segundo bimestre é: ", media2)
media3 = prova3 + trabalho3
print("Valor da media do terceiro bimestre é: ", media3)
media4 = prova4 + trabalho4
print("Valor da media do quarto bimestre é: ", media4)
nota_final = media1 + media2 + media3 + media4
print("Nota final do aluno é: ", nota_final)

if (nota_final >= 60 and nota_final <= 100):
    print("Aluno aprovado")
elif (nota_final >= 40 and nota_final < 60):
    print("Aluno em recuperação")
elif (nota_final < 40 and nota_final == 0):
    print("Aluno reprovado")
