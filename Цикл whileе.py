# Цикл while
# 1. Выведите все числа от 1 до 10 с помощью while.

print("\nЗадание 1")
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Вводите числа, пока не будет введён 0. Выведите сумму введённых чисел.

print("\nЗадание 2")
total = 0
number = int(input("Введите число, 0 — закончить: "))
while number != 0:
    total += number
    number = int(input("Введите число, 0 — закончить: "))
print("Сумма:", total)

# 3. Дано натуральное число. Посчитайте количество его цифр.

print("\nЗадание 3")
number = int(input("Введите натуральное число: "))
count = 1
while number >= 10:
    number //= 10
    count += 1
print("Количество цифр:", count)

# 4. Дано натуральное число. Найдите сумму его цифр.

print("\nЗадание 4")
number = int(input("Введите натуральное число: "))
total = 0
while number > 0:
    total += number % 10
    number //= 10
print("Сумма цифр:", total)

# 5. Дано натуральное число. Выведите его цифры в обратном порядке одним числом.

print("\nЗадание 5")
number = int(input("Введите натуральное число: "))
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
print(reversed_number)

# 6. Дано число n. Выведите все степени двойки, не превышающие n.

print("\nЗадание 6")
n = int(input("Введите число n: "))
power = 1
while power <= n:
    print(power)
    power *= 2

# 7. Запрашивайте пароль, пока пользователь не введёт правильный.

print("\nЗадание 7")
password = "12345"
entered_password = input("Введите пароль: ")
while entered_password != password:
    print("Неверный пароль")
    entered_password = input("Введите пароль: ")
print("Доступ разрешен")

# 8. Даны два натуральных числа. Найдите их наибольший общий делитель.

print("\nЗадание 8")
a = int(input("Введите первое натуральное число: "))
b = int(input("Введите второе натуральное число: "))
while b != 0:
    remainder = a % b
    a = b
    b = remainder
print("НОД:", a)

