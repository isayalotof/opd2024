numbers = range(10, 100)  # Создаем последовательность двузначных чисел
# создаю мапобъект который заполняется элементами пропущеными через лямбда функцию которая возвращает квадрат числа
# если оно делиться на 9 и считаю его сумму при помощи summ
result = sum(map(lambda x: x**2, filter(lambda x: x % 9 == 0, numbers)))

print(result)