#Inputs
hourlyRate=input("Please input the hourly rate.")
currency='R'
daylyHours=input('Enter daily hours: ')
daysOfTheWeek=input('How many days a week? ')

#Calculations 
toTalHoursPerWeek = float(daylyHours)*int(daysOfTheWeek)
toTalHoursPerMonth=(float(daylyHours)*int(daysOfTheWeek))*4
payDay=float(toTalHoursPerMonth)*int(hourlyRate)

#Overtime
if int(toTalHoursPerMonth) <= 240:
    print('Hours a days: ',daylyHours, 'hrs')
    print('Hours a week:',toTalHoursPerWeek)
    print('Hours a month:',toTalHoursPerMonth)
    print('Hourly Rate:',hourlyRate)
    print(currency+'',payDay,''+'is your gross pay for the  month.')
elif int(toTalHoursPerMonth) > 240:
    print()
    print('Hours a days: ',daylyHours, 'hrs')
    print('Hours a week:',toTalHoursPerWeek)
    print('Hours a month:', toTalHoursPerMonth)
    print('Hourly Rate:', hourlyRate)
    print(currency+'',(int(toTalHoursPerMonth - 240))* (int(hourlyRate)* 1.5)+ 240*int(hourlyRate),''+'is you gross pay for the month')