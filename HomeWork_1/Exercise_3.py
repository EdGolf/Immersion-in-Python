from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPT_AVAILABLE = 10

secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)

attempts_left = ATTEMPT_AVAILABLE

while attempts_left > 0:
    number = int(input(f"Отгадайте число (осталось попыток: {attempts_left}): "))
    if number == secret_number:
        print("Ура, это победа!")
        break
    elif secret_number > number:
        print("Загадонное числое больше.")
    else:
        print("Загадонное числое меньше.")
    attempts_left -= 1
else:
    print(f"Вы проиграли. Попробуйте еще раз. Было загадано число {secret_number}.")