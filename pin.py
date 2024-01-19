# функция проверяет простое ли число
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
# функция проверяет полиндром ли число
def is_palindrome(num):
    return str(num) == str(num)[::-1]

#   функция проверяет степень ли 2 число
def is_power_of_two(num):
    while num % 2 == 0:
        num /= 2
    return num == 1
# считываю пин
def check_pin(pinCode):
    a, b, c = pinCode.split('-')
    a = int(a)
    b = int(b)
    c = int(c)
# проверяю подходит ли пинкод
    if is_prime(a) and is_palindrome(b) and is_power_of_two(c):
        return "Корректен"
    else:
        return "Некорректен"

