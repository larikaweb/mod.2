
m = int(input('Укажите текущее число: '))
def generate_unique_password(n):
    result = ""  # Переменная для хранения результата

    # Используем множество для отслеживания уникальных пар
    unique_pairs = set()

    # Перебираем числа для поиска пар
    for i in range(1, n):
        for j in range(i, n):  # Начинаем от i, чтобы избежать дублирования пары
            # Проверяем, делится ли n на сумму пары и условие, чтобы числа следовали друг за другом
            if i != j and n % (i + j) == 0:
                pair = (i, j)
                # Проверка уникальности пары
                if pair not in unique_pairs:
                    # Добавляем пару к результату и запоминаем её как использованную
                    result += str(i) + str(j)
                    unique_pairs.add(pair)

    return result


# Примеры выполнения
password1 = generate_unique_password(9)
password2 = generate_unique_password(11)
password3 = generate_unique_password(m)

print('Пароль для числа 9 > ',password1)
print('Пароль для числа 11 > ',password2)
print('Пароль для указанного числа > ',password3)