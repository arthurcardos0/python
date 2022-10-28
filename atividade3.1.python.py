#Crie um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
#Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!"


print ("Programa para realizar saudação do dia")
turno = input("Digite seu turno, M para manhã, T para tarde e N para noite: ").upper()
match turno:
    case "M":
        print("Bom Dia!")
    case "T":
        print("Boa Tarde!")
    case "N":
        print("Boa Noite!")
    case _:
        print("Valor Inválido.")

