#importando biblioteca
import calendar
from datetime import date

#Declaração de variáveis
dia = date.today().day
mes = date.today().month
ano = date.today().year

#Tupla dos meses do ano
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

#Saida de dados 
print(f'Data Atual: {dia} de {meses[mes - 1]} de {ano}')
print('Mês atual')
print(calendar.month(ano, mes))