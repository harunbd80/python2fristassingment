#Allah Mohan

from datetime import date

d=int(input('Enter a date:'))
m=int(input('Enter a month:'))
y=int(input('Enter a year:'))

def calculate_age(cor_day,cor_month,cor_year,current_date=None): 
    
    brithday_date=date(cor_year,cor_month,cor_day)
    if not current_date:
        current_date=date.today()
    
    cor_day=current_date.day-brithday_date.day
    cor_month=current_date.month-brithday_date.month
    cor_year=current_date.year-brithday_date.year
    
    if cor_day<0:
        cor_month=cor_month-1
        cor_day=cor_day+30
    
    if cor_month<0:
        cor_year=cor_year-1
        cor_month=cor_month+12
    
    return cor_year,cor_month,cor_day

years,months,days=calculate_age(cor_day=d,cor_month=m,cor_year=y)
print(f"Your current age : {years}Year {months}Month {days}Days")