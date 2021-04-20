import winsound
import datetime

print(" Alarme ".center(30, "="))

data_marcada = input("Digite a data  (Formato: 'Dia/Mês/Ano'): ")
hora_marcada = input("Digite a hora (Formato: 'Horas:Minutos', 24 horas): ")

while True:
    hora_atual = datetime.datetime.now().strftime("%H:%M")
    data_atual = datetime.date.today().strftime("%d/%m/%Y")

    if data_atual == data_marcada and hora_atual == hora_marcada:
        winsound.Beep(2500, 10000)
        break
