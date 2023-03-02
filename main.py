import calendar

year = int(input("Введите год: "))
sum = 0

for i in range(1, 13):
    dayInMonth = calendar.monthrange(year, i)[1]
    for o in range(1, dayInMonth+1):
        sum += int(o/10) + int(o % 10)

print(str(year) + ": " + str(sum))






