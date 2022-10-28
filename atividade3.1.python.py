#Crie um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
#Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!"


print ("Pesquisa de turnos")
turno = input("Qual turno você estuda? Caso seja de manhã digite m, a tarde de v, pela noite n: ")
match turno:
    case "m":
        print("Bom Dia!")
    case "v":
        print("Boa Tarde!")
    case "n":
        print("Boa Noite!")
    case _:
        print("Valor Inválido.")
