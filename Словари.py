# Словари
# 1. Создайте словарь из трёх учеников и их оценок. Выведите оценку одного ученика по его имени.

print("\nЗадание 1")
students = {"Анастасия": 5, "Петр": 4, "Евгений": 3}
print(students["Петр"])

# 2. Дан словарь. Добавьте в него новую пару, измените значение одного из ключей, удалите другой ключ и выведите результат.

print("\nЗадание 2")
fruits = {"Банан": 100, "Апельсин": 150, "Яблоко": 80}
fruits["Груша"] = 120
fruits["Банан"] = 110
del fruits["Апельсин"]
print(fruits)

# 3. Дан словарь и ключ. Выведите значение по этому ключу, а если такого ключа нет, выведите «Нет такого ключа».

print("\nЗадание 3")
data = {"имя": "Анастасия", "возраст": 18}
key = input("Введите ключ: ")
print(data.get(key, "Нет такого ключа"))

# 4. Дан словарь. Выведите отдельно все его ключи, все значения и количество пар.

print("\nЗадание 4")
data = {"a": 10, "b": 20, "c": 30}
print("Ключи:", list(data.keys()))
print("Значения:", list(data.values()))
print("Количество пар:", len(data))

# 5. Дан словарь товаров и их цен.Выведите каждый товар и его цену с новой строки.

print("\nЗадание 5")
products = {"Хлеб": 50, "Молоко": 90, "Сыр": 250}
for product, price in products.items():
    print(product, "—", price)

# 6. Дан словарь товаров и их цен. Найдите сумму всех цен и название самого дорогого товара.

print("\nЗадание 6")
products = {"Хлеб": 50, "Молоко": 90, "Сыр": 250}
total = 0
most_expensive = list(products.keys())[0]
for product, price in products.items():
    total += price
    if price > products[most_expensive]:
        most_expensive = product
print("Сумма цен:", total)
print("Самый дорогой товар:", most_expensive)

# 7. Дана строка. Посчитайте, сколько раз в ней встречается каждый символ, и сохраните результат в словарь.

print("\nЗадание 7")
text = input("Введите строку: ")
counts = {}
for symbol in text:
    if symbol in counts:
        counts[symbol] += 1
    else:
        counts[symbol] = 1
print(counts)

# 8. Дана строка из слов через пробел. Посчитайте, сколько раз встречается каждое слово, и выведите самое частое.

print("\nЗадание 8")
text = input("Введите слова через пробел: ")
words = text.split()
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)
if words:
    most_common = words[0]
    for word in counts:
        if counts[word] > counts[most_common]:
            most_common = word
    print("Самое частое слово:", most_common)
else:
    print("Слова не введены")

# 9. Дан словарь. Создайте новый словарь,в котором ключи и значения поменяны местами.

print("\nЗадание 9")
data = {"a": 1, "b": 2, "c": 3}
new_data = {}
for key, value in data.items():
    new_data[value] = key
print(new_data)

# 10. Даны два списка одинаковой длины: страны и их столицы. Составьте из них словарь и выведите столицу страны, которую введёт пользователь.

print("\nЗадание 10")
countries = ["Россия", "Франция", "Япония"]
capitals = ["Москва", "Париж", "Токио"]
data = {}
for i in range(len(countries)):
    data[countries[i]] = capitals[i]
country = input("Введите страну с большой буквы: ").strip()
print(data.get(country, "Нет такой страны"))

