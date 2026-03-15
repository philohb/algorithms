"""
Abstract Factory pattern.

Provide an interface for creating families of related or dependent objects
without specifying their concrete classes.

https://en.wikipedia.org/wiki/Abstract_factory_pattern

Example:
    >>> factory = PetFactory()
    >>> pet = factory.create_pet("dog")
    >>> pet.speak()
    'Woof!'
    >>> toy = factory.create_toy("dog")
    >>> toy.play()
    'Squeak!'
"""


class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class DogToy:
    def play(self):
        return "Squeak!"


class CatToy:
    def play(self):
        return "Rattle!"


class PetFactory:
    """Abstract factory for creating pets and their toys."""

    _pets = {
        "dog": Dog,
        "cat": Cat,
    }

    _toys = {
        "dog": DogToy,
        "cat": CatToy,
    }

    def create_pet(self, pet_type):
        """
        Create a pet of the given type.

        :type pet_type: str
        :rtype: Dog or Cat
        """
        pet_class = self._pets.get(pet_type)
        if pet_class is None:
            raise ValueError("Unknown pet type: {}".format(pet_type))
        return pet_class()

    def create_toy(self, pet_type):
        """
        Create a toy for the given pet type.

        :type pet_type: str
        :rtype: DogToy or CatToy
        """
        toy_class = self._toys.get(pet_type)
        if toy_class is None:
            raise ValueError("Unknown pet type: {}".format(pet_type))
        return toy_class()
