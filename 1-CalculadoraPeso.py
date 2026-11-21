print("*** CALCULADORA DE PESO ***")

while True:
    altura = float(input("\nDigite a sua altura (ex: 1.50): "))
    sexo = int(input("Informe o seu sexo:\n 1 para MASCULINO\n 2 para FEMININO:\n"))
    if sexo == 1:
        pesoIdeal = (72.7 * altura) - 58
        print(f"O seu peso ideal é de {pesoIdeal:.1f}kg.")
        break
    elif sexo == 2:
        pesoIdeal = (62.1 * altura) - 44.7
        print(f"O seu peso ideal é de {pesoIdeal:.1f}kg.")
        break
    else:
        print("Valor errado! Tente novamente.")

