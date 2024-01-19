

"""создаю функцию"""
def simple_map(function, values):
    """создаю пустой список"""
    result = []
    """перебираю все элементы"""
    for value in values:
        """добавляю измененные элементы"""
        result.append(function(value))
    return result


values = [1, 3, 1, 5, 7]
operation = lambda x: x + 5
print(*simple_map(operation, values))