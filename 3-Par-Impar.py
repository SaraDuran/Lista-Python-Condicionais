# Criar um jogo de par ou ímpar, onde dois jogadores entram com seu palpite (par ou
# ímpar) e seus valores de 1 a 5. Tomar por base os nomes: Jogador 1 e Jogador 2. Caso
# um dos valores esteja fora dos parâmetros informados, mostrar uma mensagem
# informando que esta rodada não valeu. Caso contrário, informa qual jogador ganhou esta
# rodada. 

print("*** PAR OU IMPAR ***")

print('\nOlá! Para começar, digitem seus nomes:\n')

nome_jogador1 = str(input("Jogador 1:  "))
nome_jogador2 = str(input("Jogador 2:  "))

palpite_jogador1 = int(input(f"\n{nome_jogador1}, Escolha (1) para Par ou (2) para Impar:  "))

while palpite_jogador1 != 1 and palpite_jogador1 != 2:
    print("\nOpção inválida! Digite apenas 1 ou 2.")
    palpite_jogador1 = int(input(f"\n{nome_jogador1}, Escolha (1) para Par ou (2) para Impar:  "))

if palpite_jogador1 == 1:
    palpite_jogador2 = 2
else: palpite_jogador2 = 1

numero_jogador1 = int(input(f"\n{nome_jogador1}, escolha um numero de 1 a 5: "))

while numero_jogador1 < 1 or numero_jogador1 > 5:
    print("Valor inválido! Digite um número entre 1 e 5.")
    numero_jogador1 = int(input(f"\n{nome_jogador1}, escolha um numero de 1 a 5: "))


numero_jogador2 = int(input(f"\nAgora {nome_jogador2}, escolha um numero de 1 a 5: "))
while numero_jogador2 < 1 or numero_jogador2 > 5:
    print("Valor inválido! Digite um número entre 1 e 5.")
    numero_jogador2 = int(input(f"\n{nome_jogador2}, escolha um numero de 1 a 5: "))

soma = numero_jogador1 + numero_jogador2

if soma % 2 == 0:
    resultado = 1 # Par
else: 
    resultado = 2 #Impar

if palpite_jogador1 == resultado:
    print(f"\nA soma deu {soma}! {nome_jogador1} venceu a rodada!")
else: 
    print(f"\nA soma deu {soma}! {nome_jogador2} venceu a rodada!")
