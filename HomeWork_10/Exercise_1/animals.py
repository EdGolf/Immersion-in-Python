from enum import Enum

__all__ = ["Cat", "Dog", "Fish", "Animal"]


class Animal:
    def __init__(self, species: str, name: str, age: str):
        self._species = species
        self._name = name
        self._age = age

    def __str__(self):
        return f"Это животное {self._species}, зовут {self._name}, возраст {self._age} лет"


class Cat(Animal):
    __species = "Cat"
    def __init__(self, name: str, age: str, color: str):
        super().__init__(self.__species, name, age)
        self._color = color

    def __str__(self):
        return f"{super().__str__()}, цвет {self._color}"


class Dog(Animal):
    __species = "Dog"
    def __init__(self, name: str, age: str, angry: bool):
        super().__init__(self.__species, name, age)
        self._angry = angry

    def __str__(self):
        return f"{super().__str__()}, она{' не ' if not self._angry else ' '}злая"


class Fish(Animal):
    class TypeFish(Enum):
        SEA_FISH = "морская"
        FRESHWATER_FISH = "пресноводная"

    __species = "рыба"
    def __init__(self, name: str, age: str, fish_type: TypeFish):
        super().__init__(self.__species, name, age)
        self._type = fish_type

    def __str__(self):
        return f"{super().__str__()}, она {self._type.value}"


if __name__ == '__main__':
    animals = [Cat("Sen", 5, "grey"),
               Dog("Ben", 3, False),
               Fish("Perch", 1, Fish.TypeFish.FRESHWATER_FISH),
               Fish("shark", 1, Fish.TypeFish.SEA_FISH),
               Dog("Sim", 10, True)]
    for animal in animals:
        print(animal)