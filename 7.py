# Получаем целое число от пользователя и сохраняем в переменной number
number = int(input())

# Инициализируем переменную counter значением 0
counter = 0

# Запускаем цикл от 1 до number + 1
for i in range(1, number+1):
    # Проверяем, делится ли number на i без остатка
    if number % i == 0:
        # Если делится, увеличиваем счетчик counter на 1
        counter += 1

# Выводим значение counter
print(counter)
