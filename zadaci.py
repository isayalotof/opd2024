def check():
    n = int(input())
    for i in range(n):
        n1 = int(input())
        students = []
        for j in range(n1):
            fio, kol = input().split()
            students.append(kol)
        if '0' in students:
            return 'НЕТ'
    return 'ДА'


print(check())
