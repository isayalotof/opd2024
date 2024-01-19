def check():
    """считываю кол-во групп"""
    n = int(input())
    for i in range(n):
        """считываю кол-во студентов в группе"""
        n1 = int(input())
        students = []
        """считываю студентов и сохраняю кол-во предметов"""
        for j in range(n1):
            fio, kol = input().split()
            students.append(kol)
        """проверяю все ли сдали предметы"""
        if '0' in students:
            return 'НЕТ'
    return 'ДА'


print(check())
