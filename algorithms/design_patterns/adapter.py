"""
Adapter pattern.

Convert the interface of a class into another interface clients expect.
Adapter lets classes work together that couldn't otherwise because of
incompatible interfaces.

https://en.wikipedia.org/wiki/Adapter_pattern

Example:
    >>> dog = Dog()
    >>> adapted = DogAdapter(dog)
    >>> adapted.make_noise()
    'Woof!'
"""


class Dog:
    """A dog that barks."""
    def bark(self):
        return "Woof!"


class Cat:
    """A cat that meows."""
    def meow(self):
        return "Meow!"


class DogAdapter:
    """Adapt Dog to a common interface with make_noise()."""
    def __init__(self, dog):
        self._dog = dog

    def make_noise(self):
        return self._dog.bark()


class CatAdapter:
    """Adapt Cat to a common interface with make_noise()."""
    def __init__(self, cat):
        self._cat = cat

    def make_noise(self):
        return self._cat.meow()
