

print("\n*** Venda de Passagens ***\n\n")

precos = [
    ("Região Norte", "R$ 500,00", "R$ 900,00"),
    ("Região Nordeste", "R$ 350,00", "R$ 650,00"),
    ("Região Centro-Oeste", "R$ 350,00", "R$ 600,00"),
    ("Região Sul", "R$ 300,00", "R$ 550,00"),
]

print(f"{'Condição':<22} {'Ida':>12} {'Ida e volta':>14}")
print("-" * 50)

for regiao, ida, ida_volta in precos:
    print(f"{regiao:<22} {ida:>12} {ida_volta:>14}")

print("\nEscolha a região de destino:")
print("(1) Região Norte")
print("(2) Região Nordeste")
print("(3) Região Centro-Oeste")
print("(4) Região Sul\n")

while True:
    try:
        regiao = int(input("Informe o seu destino: "))
        if regiao in [1,2,3,4]:
            break
        else: 
            print("Opção inválida! Escolha apenas entre 1, 2, 3 ou 4.\n")
    except ValueError: 
        print("Entrada inválida! Digite apenas o número da opção.\n")

    
while True:
    try:
        trajeto = int(input("Informe o trajeto: \n   (1) para Ida\n   (2) para Ida e Volta\n    "))
        if trajeto in [1,2]:
            break
        else:
            print("Opção inválida! Escolha apenas entre 1 (Ida) ou 2 (Ida e Volta). \n")
    except ValueError: 
        print("Entrada inválida! Digite apenas o número da opção.\n")

if regiao == 1:
    nome_regiao = "Região  Norte"
    valor = 500.00 if trajeto == 1 else 900.00
elif regiao == 2:
    nome_regiao = "Região Nordeste"
    valor = 350.00 if trajeto == 1 else 650.00
elif regiao == 3:
    nome_regiao = "Região Centro-Oeste"
    valor = 350.00 if trajeto == 1 else 600.00
else: 
    nome_regiao = "Região Sul"
    valor = 300.00 if trajeto == 1 else 550.00

modalidade = "Ida" if trajeto == 1 else "Ida e Volta"

print("-" * 50)
print(f"Destino: {nome_regiao} | Modalidade: {modalidade}")
print(f"Valor da passagem: R$ {valor:.2f}")
