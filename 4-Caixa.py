# Implemente um programa que calcule o que deve ser pago por um produto,
# considerando o preço normal de etiqueta e a escolha da condição de pagamento. 
# Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e 
# efetuar o cálculo adequado.
# Código Condição de pagamento
#   1 – À vista em dinheiro ou cheque, recebe 10% de desconto
#   2 – À vista no cartão de crédito, recebe 15% de desconto
#   3 – Em duas vezes, preço normal de etiqueta sem juros
#   4 – Em duas vezes, preço normal de etiqueta mais juros de 10

print("*** CAIXA DE MERCADO ***\n")


while True:
    produto = input("Digite o nome do produto: ").strip()
    if produto:
        break
    print("Erro: O nome do produto não pode ficar em branco.\n")

while True:
    try:
        preco_produto = float(input("\nDigite o preço do produto: ").replace(',', '.'))
        if preco_produto > 0:
            break
        else:
            print("Erro: O preço deve ser maior que R$ 0,00.")
    except ValueError:
        print("Erro: Por favor, digite apenas números para o preço.")

parcela = preco_produto / 2
parcela_com_juros = (preco_produto * 1.10) / 2

print("\n*** FORMAS DE PAGAMENTO: ***")
print("(1) - Pagamento à vista em dinheiro/cheque (10% DE DESCONTO!)")
print("(2) - Pagamento à vista no cartão de crédito (15% DE DESCONTO!)")
print("(3) - Parcelado em duas vezes sem juros")
print("(4) - Parcelado em duas vezes com juros de 10%\n")


while True:
    try:
        forma_de_pago = int(input("SELECIONE A FORMA DE PAGAMENTO (1 a 4): "))
        if forma_de_pago in [1, 2, 3, 4]:
            break
        else:
            print("Opção inválida! Escolha apenas entre 1, 2, 3 ou 4.\n")
    except ValueError:
        print("Entrada inválida! Digite apenas o número da opção.\n")


print("-" * 40)
if forma_de_pago == 1:
    desconto_10 = preco_produto * 0.90
    print(f"Produto: {produto}")
    print(f"Você ganhou 10% de desconto! Preço final: R$ {desconto_10:.2f}")
    
elif forma_de_pago == 2:
    desconto_15 = preco_produto * 0.85
    print(f"Produto: {produto}")
    print(f"Você ganhou 15% de desconto! Preço final: R$ {desconto_15:.2f}")

elif forma_de_pago == 3:
    print(f"O preço final de {produto} (R$ {preco_produto:.2f}) será dividido em 2x de R$ {parcela:.2f} sem juros.")

elif forma_de_pago == 4:
    total_juros = preco_produto * 1.10
    print(f"O preço final de {produto} (R$ {total_juros:.2f}) será dividido em 2x de R$ {parcela_com_juros:.2f} com juros.")