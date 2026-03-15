"""
Factory Method pattern.

Define an interface for creating an object, but let subclasses decide
which class to instantiate. Factory Method lets a class defer
instantiation to subclasses.

https://en.wikipedia.org/wiki/Factory_method_pattern

Example:
    >>> dog = AnimalFactory.create_animal("dog")
    >>> dog.speak()
    'Woof!'
    >>> cat = AnimalFactory.create_animal("cat")
    >>> cat.speak()
    'Meow!'
"""


class Animal:
    """Base class for animals."""
    def speak(self):
        raise NotImplementedError


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    """Factory class to create Animal instances."""
    _animals = {
        "dog": Dog,
        "cat": Cat,
    }

    @classmethod
    def create_animal(cls, animal_type):
        """
        Create an animal of the given type.

        :type animal_type: str
        :rtype: Animal
        """
        animal_class = cls._animals.get(animal_type)
        if animal_class is None:
            raise ValueError("Unknown animal type: {}".format(animal_type))
        return animal_class()
