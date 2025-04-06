mixed_list = [1.0, "hello", 23, "world", 7, "test", 42, "python", 3, "openai"]

numbers = []
for item in mixed_list:
    if isinstance(item, (int, float)):
        numbers.append(item)

strings = []
for item in mixed_list:
    if isinstance(item, str):
        strings.append(item)

max_value = None
min_value = None
for item in mixed_list:
    if isinstance(item, (int, float)):
        if max_value is None or item > max_value:
            max_value = item
        if min_value is None or item < min_value:
            min_value = item

avg_value = 0
if len(numbers) > 0:
    total = 0
    for num in numbers:
        total += num
    avg_value = total / len(numbers)

longest_word = ""
shortest_word = None
for item in mixed_list:
    if isinstance(item, str):
        if shortest_word is None:
            shortest_word = item
        if len(item) > len(longest_word):
            longest_word = item
        if len(item) < len(shortest_word):
            shortest_word = item

search = input("Введите слово для поиска: ")
found = False
for item in mixed_list:
    if isinstance(item, str) and item == search:
        found = True
        break

print("Исходный список:", mixed_list)
print("Только числа:", numbers)
print("Только строки:", strings)
if max_value is not None:
    print("Максимальное число:", max_value)
if min_value is not None:
    print("Минимальное число:", min_value)
if len(numbers) > 0:
    print("Среднее значение чисел:", avg_value)
if longest_word:
    print("Самое длинное слово:", longest_word)
if shortest_word is not None:
    print("Самое короткое слово:", shortest_word)
if found:
    print("Слово", search, "найдено в списке.")
else:
    print("Слово", search, "не найдено в списке.")