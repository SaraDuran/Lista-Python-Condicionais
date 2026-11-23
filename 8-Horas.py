from datetime import datetime, timedelta


def eh_bissexto(ano: int) -> bool:
    # Etapa 1
    if ano % 4 == 0:
        # Etapa 2
        if ano % 100 == 0:
            # Etapa 3
            if ano % 400 == 0:
                return True  
            else:
                return False  
        else:
            return True  
    else:
        return False  


dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
hora = int(input("Hora (0-23): "))
minuto = int(input("Minuto (0-59): "))
segundo = int(input("Segundo (0-59): "))

data_inicial = datetime(ano, mes, dia, hora, minuto, segundo)

print("\nO que você deseja acrescentar?")
print("1 - Dias | 2 - Meses (30 dias) | 3 - Anos | 4 - Horas | 5 - Minutos | 6 - Segundos")
campo = int(input("Escolha a opção (1 a 6): "))
qtd = int(input("Quantidade a acrescentar: "))

if campo == 1:
    nova_data = data_inicial + timedelta(days=qtd)
elif campo == 2:
    # Aproximação padrão de 30 dias por mês quando não há calendário fixo
    nova_data = data_inicial + timedelta(days=qtd * 30)
elif campo == 3:
    # Soma anos considerando bissexto (29/fev -> 28/fev se o ano destino não for bissexto)
    ano_final = data_inicial.year + qtd
    dia_final = data_inicial.day
    if data_inicial.month == 2 and data_inicial.day == 29 and not eh_bissexto(ano_final):
        dia_final = 28
    nova_data = data_inicial.replace(year=ano_final, day=dia_final)
elif campo == 4:
    nova_data = data_inicial + timedelta(hours=qtd)
elif campo == 5:
    nova_data = data_inicial + timedelta(minutes=qtd)
elif campo == 6:
    nova_data = data_inicial + timedelta(seconds=qtd)
else:
    nova_data = None

if nova_data:
    print("\nNova data e hora:", nova_data.strftime("%d/%m/%Y %H:%M:%S"))
    print(f"Ano {nova_data.year} é bissexto? {'Sim (366 dias)' if eh_bissexto(nova_data.year) else 'Não (365 dias)'}")
else:
    print("Opção inválida.")