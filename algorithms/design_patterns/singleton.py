"""
Singleton pattern.

The singleton pattern ensures a class has only one instance and provides
a global point of access to it.

https://en.wikipedia.org/wiki/Singleton_pattern

Example:
    >>> class MyClass(metaclass=SingletonMeta):
    ...     pass
    >>> a = MyClass()
    >>> b = MyClass()
    >>> a is b
    True
"""


class SingletonMeta(type):
    """
    A metaclass that creates a Singleton base type when called.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
