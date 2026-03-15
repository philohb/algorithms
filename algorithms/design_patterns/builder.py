"""
Builder pattern.

Separate the construction of a complex object from its representation
so that the same construction process can create different representations.

https://en.wikipedia.org/wiki/Builder_pattern

Example:
    >>> builder = PizzaBuilder()
    >>> pizza = builder.set_size("large").add_cheese().add_pepperoni().build()
    >>> pizza.size
    'large'
    >>> "cheese" in pizza.toppings
    True
"""


class Pizza:
    """A pizza built by PizzaBuilder."""
    def __init__(self):
        self.size = None
        self.toppings = []

    def __repr__(self):
        return "Pizza(size={}, toppings={})".format(self.size, self.toppings)


class PizzaBuilder:
    """Builder for constructing Pizza objects step by step."""
    def __init__(self):
        self._pizza = Pizza()

    def set_size(self, size):
        self._pizza.size = size
        return self

    def add_cheese(self):
        self._pizza.toppings.append("cheese")
        return self

    def add_pepperoni(self):
        self._pizza.toppings.append("pepperoni")
        return self

    def add_mushrooms(self):
        self._pizza.toppings.append("mushrooms")
        return self

    def build(self):
        """
        Return the constructed Pizza and reset the builder.

        :rtype: Pizza
        """
        pizza = self._pizza
        self._pizza = Pizza()
        return pizza
