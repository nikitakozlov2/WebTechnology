import random

while True:
    secret = random.randint(1, 100)
    attempts = 0
    print("Загадано число от 1 до 100. Попробуйте угадать!")
    while True:
        guess_input = input("Введите ваше предположение: ")
        if not guess_input.isdigit():
            print("Пожалуйста, введите целое число.")
            continue
        guess = int(guess_input)
        attempts += 1
        if guess < secret:
            print("Загаданное число больше.")
        elif guess > secret:
            print("Загаданное число меньше.")
        else:
            print("Вы угадали число с", attempts, "попытки!")
            break
    play_again = input("Сыграть еще раз? (да/нет): ").strip().lower()
    if play_again != "да":
        print("Игра завершена.")
        break