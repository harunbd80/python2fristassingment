from datetime import date

date_of_brith=int(input('Enter a date of brith year :'))

today_date=date.today().year

print('Your current Age :',int(today_date)-date_of_brith)