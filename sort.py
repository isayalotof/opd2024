def sorted2(data, key=None):
    if key is None:
        key = lambda x: -x

    # Создаем копию исходных данных, чтобы не изменять их
    data_copy = [sorted(sublist, key=key) for sublist in data]

    # Сортируем вложенные списки по последнему элементу каждого из них
    sorted_data = sorted(data_copy, key=lambda x: x[-1] if x else float('-inf'))

    return sorted_data

# Пример использования
data = [[6, 5, 4], [3, 2], [1]]
key = lambda x: x
print(sorted2(data, key=key))

