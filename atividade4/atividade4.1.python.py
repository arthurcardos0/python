#Crie um programa para calcular as notas obtidas pelo aluno do
#ensino médio, deverá mostrar mensagem para ser digitado a
#nota do 1º, 2º, 3º e 4º bimestre. Após deverá mostrar na tela se o aluno foi aprovado, se está em recuperação ou foi reprovado
#sem chance de recuperação.
#• Lembrando que cada bimestre vale 25 pontos num total anual de 100 pontos.

print("Programa de lançamento de notas")

print("Digite números válidos soemnete entre 0 e 25")
bimestre1 = float(input("Valor da nota referente ao 1 bimestre: "))
bimestre2 = float(input("Valor da nota referente ao 2 bimestre: "))
bimestre3 = float(input("Valor da nota referente ao 3 bimestre: "))
bimestre4 = float(input("Valor da nota referente ao 4 bimestre: "))

nota_final = bimestre1 + bimestre2 + bimestre3 + bimestre4
print("A nota final do aluno é: ", nota_final)

if (nota_final >= 60 and nota_final <= 100):
    print("Aluno aprovado")
elif (nota_final <= 40 and nota_final < 60):
    print("Aluno em recuperação")
elif (nota_final < 40 and nota_final == 0):
    print("Aluno reprovado")



