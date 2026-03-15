"""
Decorator pattern.

Attach additional responsibilities to an object dynamically.
Decorators provide a flexible alternative to subclassing for extending
functionality.

https://en.wikipedia.org/wiki/Decorator_pattern

Note: This is the object-oriented Decorator design pattern, which is
different from Python's @decorator syntax (though related in concept).

Example:
    >>> component = TextComponent("Hello")
    >>> bold = BoldDecorator(component)
    >>> bold.render()
    '<b>Hello</b>'
"""


class TextComponent:
    """A simple text component."""
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class TextDecorator:
    """Base decorator that wraps a TextComponent."""
    def __init__(self, component):
        self._component = component

    def render(self):
        return self._component.render()


class BoldDecorator(TextDecorator):
    """Decorator that wraps text in bold tags."""
    def render(self):
        return "<b>{}</b>".format(self._component.render())


class ItalicDecorator(TextDecorator):
    """Decorator that wraps text in italic tags."""
    def render(self):
        return "<i>{}</i>".format(self._component.render())
