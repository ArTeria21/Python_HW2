#Создаем переменные хранящие сумму всех чисел и их к-во
sum = 0
amount = 0

while True:
    number = int(input())
    if number != 0: #Пока не введен 0, обновляем значение переменной
        sum += number
        amount += 1
    else:
        break

print("Среднее арифметическое =", sum / amount)