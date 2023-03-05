iterations = int(input("Введите количество чисел: ")) #Получаем к-во чисел
checker = "NO" #Сразу создаем переменную, хранящую информацию о к-ве нулей
for _ in range(iterations):
    number = int(input("Введите число: ")) #Каждую иттераию цикла спрашиваем число
    if number == 0: #Если хоть одно число равно 0, заменяем значение checker
        checker = "YES"

print(checker)
