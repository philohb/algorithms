"""
Prototype pattern.

Specify the kinds of objects to create using a prototypical instance,
and create new objects by copying this prototype.

https://en.wikipedia.org/wiki/Prototype_pattern

Example:
    >>> prototype = Prototype()
    >>> prototype.register("default_car", {"brand": "Unknown", "speed": 0})
    >>> car = prototype.clone("default_car")
    >>> car["brand"]
    'Unknown'
"""

import copy


class Prototype:
    """
    A registry of prototypical instances that can be cloned
    to produce new objects.
    """
    def __init__(self):
        self._registry = {}

    def register(self, name, obj):
        """
        Register a prototypical object under the given name.

        :type name: str
        :type obj: object
        """
        self._registry[name] = obj

    def unregister(self, name):
        """
        Remove a prototype from the registry.

        :type name: str
        """
        del self._registry[name]

    def clone(self, name, **kwargs):
        """
        Clone the registered prototype and optionally update attributes.

        :type name: str
        :rtype: object
        """
        obj = copy.deepcopy(self._registry[name])
        obj.update(kwargs)
        return obj
