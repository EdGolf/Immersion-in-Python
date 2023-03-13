MIN_VALUE = 1
MAX_VALUE = 100_000

number = int(input(f"Введите число от {MIN_VALUE} до {MAX_VALUE}: "))

if MIN_VALUE <= number <= MAX_VALUE:
    for divider in range(2, int(number ** 0.5)):
        if number % divider == 0:
            print(f"Число {number} составное")
            break
    else:
        print(f"Число {number} простое")
else:
    print("Введенное число вне диапазона")