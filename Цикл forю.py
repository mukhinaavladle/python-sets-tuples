# Цикл for
# 1. Выведите все числа от 1 до 10.

print("\nЗадание 1")
for i in range(1, 11):
    print(i)

# 2. Выведите все чётные числа от 2 до 50.

print("\nЗадание 2")
for i in range(2, 51, 2):
    print(i)

# 3. Выведите числа от 10 до 1 в порядке убывания.

print("\nЗадание 3")
for i in range(10, 0, -1):
    print(i)

# 4. Дано число n. Найдите сумму всех чисел от 1 до n.

print("\nЗадание 4")
n = int(input("Введите натуральное число n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Сумма:", total)

# 5. Дано число n. Найдите его факториал.

print("\nЗадание 5")
n = int(input("Введите целое число n: "))
if n < 0:
    print("Факториал отрицательного числа не определён")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("Факториал:", factorial)

# 6. Дано число n. Выведите таблицу умножения на n от 1 до 10.

print("\nЗадание 6")
n = int(input("Введите число n: "))
for i in range(1, 11):
    print(n, "*", i, "=", n * i)

# 7. Дан список чисел. Посчитайте, сколько в нём положительных чисел.

print("\nЗадание 7")
numbers = [-5, 3, 0, 8, -2, 10]
count = 0
for number in numbers:
    if number > 0:
        count += 1
print("Количество положительных чисел:", count)

# 9. Дан список чисел. Найдите наибольший элемент, не используя max().

print("\nЗадание 9")
numbers = [4, -2, 15, 7, 0]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Наибольший элемент:", largest)
