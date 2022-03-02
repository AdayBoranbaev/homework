name = input("What is your name? ")
print("My name is", name, ".")
age = int(input("What is your age?"))
print("I am", age,"years old")
country = input("Where are you from?")
print("I am from", country)

#---------------------------------------------------

time = int(input("Введите колиечство секунд"))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время на часах {hours:02}:{minutes:02}:{seconds:02}")

#---------------------------------------------------


n = int(input("Enter n "))
nn = n * 10 + n
nnn = n * 100 + n * 10 + n
print(n + nn + nnn)

#---------------------------------------------------

num_init = int(input("Введите целое положительное число"))
greatest_dig = 0
num = num_init

while num > 0:
    digit = num % 10
    if digit > greatest_dig:
        greatest_dig = digit
        if greatest_dig == 9:
            break
    num = num // 10
print(f"Наибольшая цифра в числе {num_init} равна {greatest_dig}")


#---------------------------------------------------


revenue = int(input("Введите вашу прибыль "))
cost = int(input("Введите ваши издержки "))
profitability = revenue // cost * 100
if revenue > cost:
    print("Ваша компания находится в плюсе ")
    print("Ваша рентабельность к выручке составляет ", profitability , "%")
    staff = int(input("Введите количество ваших сотрудников "))
    print("Ваша прибыль на одного сотрудника составляет ", revenue  // staff, "рублей")
elif revenue < cost:
    print("Ваша компания находится в минусе ")
elif revenue == cost:
    print("Прибыль и издержки компании равны ")

#---------------------------------------------------

while True:
    days = 1
    start_km = float(input("Стартовый результат: "))
    last_km = float(input("Финальный результат: "))
    if start_km <= 0 or last_km < 0:
        print("Результаты должны быть больше нуляюСтартовое значение !=0.")
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1
            print(f"Спортсмен добьется результатов за {days} дней")
            break
