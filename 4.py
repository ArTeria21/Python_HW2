# Инициализируем начальные значения переменных
max_len = 1
counter = 1
last = None
direction = None

# Бесконечный цикл для ввода чисел пользователем
while True:
    number = int(input("Введите число: "))

    # Если число равно нулю, то выходим из цикла
    if number == 0:
        break

    # Если это первое число, записываем его и продолжаем цикл
    if last is None:
        last = number
        continue

    # Определяем направление последовательности
    diff = number - last
    if diff > 0:
        curr_dir = "Up"
    elif diff < 0:
        curr_dir = "Down"
    else:
        curr_dir = None

    # Если направление не изменилось, увеличиваем счетчик
    if curr_dir == direction or direction is None:
        counter += 1
    else:
        # Если направление изменилось, проверяем максимальную длину
        if counter > max_len:
            max_len = counter
        counter = 2  # начинаем новую последовательность с текущего и предыдущего числа

    # Обновляем значения переменных для следующей итерации
    last = number
    direction = curr_dir

# Проверяем максимальную длину последовательности после выхода из цикла
if counter > max_len:
    max_len = counter

# Выводим наибольшую длину монотонно возрастающей или убывающей последовательности
print(max_len)
