s = input("Введите строку: ")
total_chars = len(s)
letters = 0
digits = 0
specials = 0
for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        specials += 1
print("Общее количество символов:", total_chars)
print("Количество букв:", letters)
print("Количество цифр:", digits)
print("Количество специальных символов:", specials)