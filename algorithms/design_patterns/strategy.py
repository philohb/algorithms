"""
Strategy pattern.

Define a family of algorithms, encapsulate each one, and make them
interchangeable. Strategy lets the algorithm vary independently from
clients that use it.

https://en.wikipedia.org/wiki/Strategy_pattern

Example:
    >>> ctx = Context(AddStrategy())
    >>> ctx.execute(3, 4)
    7
    >>> ctx.strategy = MultiplyStrategy()
    >>> ctx.execute(3, 4)
    12
"""


class AddStrategy:
    """Strategy that adds two numbers."""
    def execute(self, a, b):
        return a + b


class SubtractStrategy:
    """Strategy that subtracts two numbers."""
    def execute(self, a, b):
        return a - b


class MultiplyStrategy:
    """Strategy that multiplies two numbers."""
    def execute(self, a, b):
        return a * b


class Context:
    """Context that uses a strategy to perform an operation."""
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, a, b):
        """
        Execute the current strategy with the given operands.

        :type a: int or float
        :type b: int or float
        :rtype: int or float
        """
        return self.strategy.execute(a, b)
