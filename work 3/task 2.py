search_str = input("Искомая подстрока: ")
replace_str = input("Новая подстрока: ")
try:
    f = open("example.txt", "r", encoding="utf-8")
    content = f.read()
    f.close()
except FileNotFoundError:
    print("Файл не найден.")
else:
    new_content = content.replace(search_str, replace_str)
    try:
        f = open("example.txt", "w", encoding="utf-8")
        f.write(new_content)
        f.close()
        print("Замена выполнена успешно.")
    except Exception:
        print("Ошибка при записи в файл.")