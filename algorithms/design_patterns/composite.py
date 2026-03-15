"""
Composite pattern.

Compose objects into tree structures to represent part-whole hierarchies.
Composite lets clients treat individual objects and compositions of objects
uniformly.

https://en.wikipedia.org/wiki/Composite_pattern

Example:
    >>> leaf1 = Leaf("A")
    >>> leaf2 = Leaf("B")
    >>> composite = Composite("root")
    >>> composite.add(leaf1)
    >>> composite.add(leaf2)
    >>> composite.get_info()
    'root: [A, B]'
"""


class Component:
    """Base component that declares the common interface."""
    def __init__(self, name):
        self.name = name

    def get_info(self):
        raise NotImplementedError


class Leaf(Component):
    """A leaf node that has no children."""
    def get_info(self):
        return self.name


class Composite(Component):
    """A composite node that can contain children."""
    def __init__(self, name):
        super().__init__(name)
        self._children = []

    def add(self, component):
        """
        Add a child component.

        :type component: Component
        """
        self._children.append(component)

    def remove(self, component):
        """
        Remove a child component.

        :type component: Component
        """
        self._children.remove(component)

    def get_info(self):
        """
        Return info about this composite and its children.

        :rtype: str
        """
        children_info = ", ".join(c.get_info() for c in self._children)
        return "{}: [{}]".format(self.name, children_info)
