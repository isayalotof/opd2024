def check_digit(x):
    for d in '1234567890':
        x = str(x).replace(d, '')
    return x

def password_level(password):
# проверка длинны
    if len(password) < 6:
        return "Недопустимый пароль"
# проверка на то что пароль состоит только из цифр
    if password.isdigit():
        return "Ненадежный пароль"
# проверка на то что пароль состоит из букв одного регистра
    if (password.isupper() or password.islower()) and (check_digit(password) == password):
        return "Ненадежный пароль"
# так как уже проверили что регистр разный просто проверяем на то что пароль только из букв
    if password.isalpha():
        return "Слабый пароль"
#   если пароль в нижнем регистре == изначальному => пароль состоит из
#    букв одного регистра и цифр
    if password.lower() == password:
        return "Слабый пароль"
#   аннологично с предыдущем пунктом
    if password.upper() == password:
        return "Слабый пароль"
# если ничего не подошло значит пароль надежный
    return "Надежный пароль"


print(password_level('a54354F'))