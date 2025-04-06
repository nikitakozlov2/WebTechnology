try:
    f = open("example.txt", "r", encoding="utf-8")
    text = f.read()
    f.close()
except FileNotFoundError:
    print("Файл не найден.")
else:
    total = 0
    for ch in text:
        if ch.isdigit():
            total += int(ch)
    print("Сумма цифр в файле:", total)