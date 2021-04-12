import winsound
import datetime

print(" Alarme ".center(30, "="))

data_marcada = input("Digite a data  (Formato: 'Dia/Mês/Ano'): ")
hora_marcada = input("Digite a hora (Formato: 'Horas:Minutos', 24 horas): ")

while True:
    hora = datetime.datetime.now()
    data = datetime.date.today()

    if data.strftime("%d/%m/%Y") == data_marcada and hora.strftime("%H:%M") == hora_marcada:
        winsound.Beep(2500, 10000)
        break
