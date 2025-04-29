def somar (a, b):
    resultado = a + b
    return resultado

#chamar função

a= int(input("Digite o valor de A: "))
b= int(input("Digite o valor de B: "))

x = somar(a, b)
print(f"O resultado da soma é {x}")