# Crie um programa que receba cinco produtos em variáveis constantes.

iphone = 2980
samsung = 2540
tablet = 1950
ps5 = 2100
notebook = 2350

qtdiphone = int(input("Digite a quantidade de Iphone desejaveis: "))
qtdsamsung = int(input("Digite a quantidade de Samsung desejaveis: "))
qtdtablet = int(input("Digite a quantidade de Tablet desejaveis: "))
qtdps5 = int(input("Digite a quantidade de PS5 desejaveis: "))
qtdnotebook = int(input("Digite a quantidade de Notebook desejaveis: "))

#total comum
total = (qtdiphone+iphone) + (qtdsamsung+samsung) + (qtdtablet+tablet) + (qtdps5+ps5) + (qtdnotebook+notebook)
print ("O valot total da compra é: ", format(total))

#parcela de 3 vezes sem juros
parcela3 = round (total / 3, 2)
print ("O valor parcelado em 3 vezes é: ", format(parcela3))

#parcela6 de 6 vezes com acrescimos de 5%
parcela6 = round ((total+1.05) / 3, 2)
print ("O valor parcelado com acrescimo de 5% é: ", format (parcela6))

#valor com 10% de desconto a vista
desconto = round (total - (total*0.1))
print ("O valor com desconto de 10% pagando a vista é: ", format(desconto))


