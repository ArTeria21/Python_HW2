# Инициализируем начальные значения переменных
max_len = 1
counter = 1
last = 0
direction = 0  # Указывает направление роста

# Бесконечный цикл для ввода чисел пользователем
while True:
    number = int(input("Введите число: "))

    # Если число равно нулю, то выходим из цикла
    if number == 0:
        break
    else:
        # Если last равно 0, то записываем в него значение number и продолжаем цикл
        if last == 0:
            last = number
            continue
        # Если число больше предыдущего и direction указывает на рост или не определено,
        # увеличиваем счетчик и проверяем, не превысил ли максимальную длину
        if number > last and (direction == "Up" or direction == 0):
            direction = "Up"
            counter += 1
            if counter > max_len:
                max_len = counter
        # Если число меньше предыдущего и direction указывает на уменьшение или не определено,
        # увеличиваем счетчик и проверяем, не превысил ли максимальную длину
        elif number < last and (direction == "Down" or direction == 0):
            direction = "Down"
            counter += 1
            if counter > max_len:
                max_len = counter
        # Если число не соответствует текущему направлению или direction не определено,
        # обнуляем счетчик и продолжаем цикл
        else:
            counter = 1
            continue
        # Записываем значение number в last для следующей итерации цикла
        last = number

# Выводим наибольшую длину монотонно возрастающей или убывающей последовательности
print(max_len)
