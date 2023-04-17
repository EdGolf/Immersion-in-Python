from random import randint
from typing import Callable

NUM_MIN = 1
NUM_MAX = 100
TRIES_MIN = 1
TRIES_MAX = 10

__all__ = ["gues_game"]


def check_arguments(func):
    def wrapper(secret, num_tries, *args, **kwargs):
        if secret < NUM_MIN or secret > NUM_MAX:
            secret = randint(NUM_MIN, NUM_MAX)
        if num_tries < TRIES_MIN or num_tries > TRIES_MAX:
            num_tries = randint(TRIES_MIN, TRIES_MAX)
        return func(secret, num_tries, *args, **kwargs)

    return wrapper


@check_arguments
def guessing_game(secret: int, num_tries) -> Callable[[int], tuple[bool, int]]:
    print(f"Угадайте число {secret} за {num_tries} попыток")

    def game_fun(user_num: int) -> tuple[bool, int]:
        nonlocal num_tries, secret
        if user_num == secret:
            return True, 0
        num_tries -= 1

        return False, num_tries

    return game_fun


if __name__ == '__main__':
    game = guessing_game(555, 5)
    while True:
        num = int(input("Введите число: "))
        res, tries = game(num)
        if res:
            print("Верно!")
            break
        if tries == 0:
            print("Попыток не осталось")
            break
        print(f"Попыток осталось: {tries}")