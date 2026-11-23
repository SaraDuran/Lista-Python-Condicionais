meses = {
    1: ("jan", "janeiro"),
    2: ("fev", "fevereiro"),
    3: ("mar", "março"),
    4: ("abr", "abril"),
    5: ("mai", "maio"),
    6: ("jun", "junho"),
    7: ("jul", "julho"),
    8: ("ago", "agosto"),
    9: ("set", "setembro"),
    10: ("out", "outubro"),
    11: ("nov", "novembro"),
    12: ("dez", "dezembro"),
}

dia = int(input("Dia: "))
mes = int(input("Mês (1-12): "))
ano = int(input("Ano (4 dígitos, ex: 1990): "))

print("\nCódigo de Exibição de Data:")
print("1 – Data simples. Ex.: 10/08/1990")
print("2 – Data abreviada. Ex.: 10/ago/1990")
print("3 – Data completa. Ex.: 10 de agosto de 1990")

opcao = int(input("\nEscolha o formato (1, 2 ou 3): "))
abrev, extenso = meses[mes]

if opcao == 1:
    print(f"{dia:02d}/{mes:02d}/{ano:04d}")
elif opcao == 2:
    print(f"{dia:02d}/{abrev}/{ano:04d}")
elif opcao == 3:
    print(f"{dia:02d} de {extenso} de {ano:04d}")
else:
    print("Opção inválida.")