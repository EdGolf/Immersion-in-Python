import Exercise_1


class AnimalFactory:
    def __init__(self, animal_type: type, *args, **kwargs):
        if not issubclass(animal_type, Exercise_1.Animal):
            raise ValueError(f"Animal {animal_type.__name__} does not exist.")
        self._animal_type = animal_type
        self._args = args
        self._kwargs = kwargs
        self._animal = None

    def get_animal(self):
        if not self._animal:
            self._animal = self._animal_type(*self._args, **self._kwargs)
        return self._animal


if __name__ == '__main__':
    cat_factory = AnimalFactory(Exercise_1.Cat, "Sen", 3, "Grey")
    cat1 = cat_factory.get_animal()
    print(cat1)

    dog_factory = AnimalFactory(Exercise_1.Dog, name="Ben", age=3, angry=True)
    dog1 = dog_factory.get_animal()
    print(dog1)

    fish_factory = AnimalFactory(Exercise_1.Fish, "Perch", 1, Exercise_1.Fish.TypeFish.FRESHWATER_FISH)
    fish1 = fish_factory.get_animal()
    print(fish1)

    other_factory = AnimalFactory(object, 1, 3, 2)
    other = other_factory.get_animal()
    print(other)