
print("*** Calculo de IMC – Índice de Massa Corporal ***")

altura = float(input("\nDigite sua altura (ex: 1.50):  "))
peso = float(input("\nDigite seu peso (ex: 63.2):  "))
imc = peso / (altura ** 2)

print(f"\nSeu IMC é {imc:.2f}")

if imc < 18.5:
    print("\nVocê está abaixo do peso.")
elif imc < 25:
    print("\nVocê está no peso normal.")
elif imc < 30:
    print("\nVocê está acima do peso.")
else:
    print("\nVocê está obeso, recomendo comprar um tênis.")