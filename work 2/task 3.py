n = int(input("Введите число: "))
print("Делители числа", n, ":")
for i in range(1, n+1):
    if n % i == 0:
        print(i)