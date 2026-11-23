digitos = []
print("Digite cada um dos 11 dígitos do CPF (0 a 9):")
for i in range(1, 12):
    d = int(input(f"Dígito {i}: "))
    digitos.append(d)

# primeiro digito verificador (usa os 9 primeiros digitos e pesos de 10 a 2)
soma_1 = 0
peso = 10
for i in range(9):
    soma_1 += digitos[i] * peso
    peso -= 1

resto_1 = (soma_1 * 10) % 11
if resto_1 == 10:
    resto_1 = 0

# segundo digito verificador (usa os 10 primeiros digitos e pesos de 11 a 2)
soma_2 = 0
peso = 11
for i in range(10):
    soma_2 += digitos[i] * peso
    peso -= 1

resto_2 = (soma_2 * 10) % 11
if resto_2 == 10:
    resto_2 = 0

cpf_formatado = (
    f"{digitos[0]}{digitos[1]}{digitos[2]}."
    f"{digitos[3]}{digitos[4]}{digitos[5]}."
    f"{digitos[6]}{digitos[7]}{digitos[8]}-"
    f"{digitos[9]}{digitos[10]}"
)

if resto_1 == digitos[9] and resto_2 == digitos[10]:
    print(f"\nO CPF {cpf_formatado} é VÁLIDO.")
else:
    print(f"\nO CPF {cpf_formatado} é INVÁLIDO.")