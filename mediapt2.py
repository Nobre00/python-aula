print("Bem vindo ao primeiro contato com python!!")
numero1 = int( input ("Digite seu primeiro número: "))
numero2 = int( input ("Digite seu segundo número: "))

media = (numero1 + numero2) / 2
#cálculo da média

if media > 7:
    print(f"Sua média foi de {media} está aprovado!!")
elif media < 7 and media > 4:
    print(f"Sua média foi de {media} você está na final!!")
else:
    print(f"Sua média foi de {media} você foi reprovado!!")


