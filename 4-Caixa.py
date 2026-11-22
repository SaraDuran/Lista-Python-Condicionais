# Implemente um programa que calcule o que deve ser pago por um produto,
# considerando o preço normal de etiqueta e a escolha da condição de pagamento. 
# Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e 
# efetuar o cálculo adequado.
# Código Condição de pagamento
#   1 – À vista em dinheiro ou cheque, recebe 10% de desconto
#   2 – À vista no cartão de crédito, recebe 15% de desconto
#   3 – Em duas vezes, preço normal de etiqueta sem juros
#   4 – Em duas vezes, preço normal de etiqueta mais juros de 10

print("*** CAIXA DE MERCADO ***\n");

produto = str(input("Digite o nome do produto: "))
preco_produto = float(input("\nDigite o preço do produto: "))
parcela = preco_produto/2
parcela_com_juros = (preco_produto + (preco_produto * 0.10))/2

print("\n*** FORMAS DE PAGAMENTO: ***")
print("\n(1) - Pagamento à vista em dinheiro/cheque (10% DE DESCONTO!)")
print("\n(2) - Pagamento à vista no cartão de crédito (15% DE DESCONTO!)")
print("\n(3) - Parcelado em duas vezes sem juros")
print("\n(4) - Parcelado em duas vezes com juros de 10%")


forma_de_pago = int(input("SELECIONE A FORMA DE PAGAMENTO: "))
if forma_de_pago == 1:
    desconto_10 = preco_produto - (preco_produto * 0.10)
    print(f"Você ganhou 10% de desconto! O preço final da sua compra é de R${desconto_10:.2f}")
    
elif forma_de_pago == 2:
    desconto_15 = preco_produto - (preco_produto * 0.15)
    print(f"Você ganhou 15% de desconto! O preço final da sua compra é de R${desconto_15}")

elif forma_de_pago == 3:
    print(f"O preço final de {produto} será dividido em duas vezes de R${parcela}.")
else:
    print(f"O preço final de {produto} será dividido em duas vezes de R${parcela_com_juros}.")






