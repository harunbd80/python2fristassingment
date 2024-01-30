from datetime import datetime

date_time=datetime.now()
#practice-01
current_date=date_time.strftime('%d-%m-%Y')
current_time=date_time.strftime('%A%I:%M%p')
print(f"(project-01),,,Today Date :{current_date}\n Current Time:{current_time}")

#practice-02
current_date=date_time.strftime('%d-%b-%y')
current_time=date_time.strftime('%H:%M%p')
print(f"(project-02),,,Today Date :{current_date}\n Current International Time:{current_time}")

#practice-03
current_date=date_time.strftime('%B-%d-%j,')
current_time=date_time.strftime('%H:%M:%S')
print(f"(project-03),,,Today Date :{current_date}\n Current International Time:{current_time}")

#practice-04
current_date=date_time.strftime('%Y/%B/%d')
current_time=date_time.strftime('%I:%M%p')
print(f"(project-04),,,Today Date :{current_date}\n Current Time:{current_time}")

#practice-05
current_date=date_time.strftime('year:%Y,month:%m,day:%d')
current_time=date_time.strftime('%A%I:%M%p')
print(f"(project-05),,,Today Date :{current_date}\n Current Time:{current_time}")
