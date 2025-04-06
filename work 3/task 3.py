try:
    shift = int(input("Введите сдвиг: "))
except ValueError:
    print("Некорректный сдвиг.")
else:
    try:
        f = open("example.txt", "r", encoding="utf-8")
        text = f.read()
        f.close()
    except FileNotFoundError:
        print("Файл не найден.")
    else:
        encrypted_text = ""
        for ch in text:
            if 'a' <= ch <= 'z':
                encrypted_text += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            elif 'A' <= ch <= 'Z':
                encrypted_text += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += ch
        try:
            f_out = open("encrypted_example.txt", "w", encoding="utf-8")
            f_out.write(encrypted_text)
            f_out.close()
            print("Текст зашифрован в файл encrypted_example.txt.")
        except Exception:
            print("Ошибка при сохранении файла.")