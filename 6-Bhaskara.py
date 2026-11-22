import math


print("*** BHASKARA ***\n")
print("Olá! Vamos calcular equações de segundo grau? Vem comigo!")

while True:
    try:
        coeficiente_A = float(input("\nPara começar, atribua um valor para A: "))
        if coeficiente_A != 0:
            break
        else: 
            print("Se A for igual a zero, a equação passa a ser uma equação de segundo grau. \nPor favor, insira um valor válido")
    except ValueError:
        print("\nPor favor, insira um valor numerico válido")

coeficiente_B = float(input("\nagora, atribua um valor para B: "))
coeficiente_C = float(input("\nPor ultimo, atribua um valor para C: "))
delta = coeficiente_B **2 - (4 * (coeficiente_A * coeficiente_C))

if delta <  0:
    print("\nNão há raizes reais")
elif delta == 0:
    x1 = (-coeficiente_B + math.sqrt(delta)) / 2 * coeficiente_A
    print(f"\nExiste uma unica raiz real ou duas raizes iguais: {x1}")
else:
    x1 = (-coeficiente_B + math.sqrt(delta)) / 2 * coeficiente_A
    x2= (-coeficiente_B - math.sqrt(delta)) / 2 * coeficiente_A
    print(f"\nExistem duas raizes reais distintas: x1= {x1:.1f} e x2= {x2:.1f}")

#A não pode ser 0 
# Se delta < 0, Não ha raizes reais
#se delta= 0 existe una unica raiz real ou duas raizes iguais
# se delta > 0 existen duas raizes reais distintas

