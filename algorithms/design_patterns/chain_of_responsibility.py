"""
Chain of Responsibility pattern.

Avoid coupling the sender of a request to its receiver by giving more
than one object a chance to handle the request. Chain the receiving
objects and pass the request along the chain until an object handles it.

https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern

Example:
    >>> h1 = ConcreteHandler(1)
    >>> h2 = ConcreteHandler(2)
    >>> h3 = ConcreteHandler(3)
    >>> h1.set_next(h2).set_next(h3)
    >>> h1.handle(2)
    'Handler 2 handled request 2'
    >>> h1.handle(4) is None
    True
"""


class Handler:
    """Base handler in the chain."""
    def __init__(self):
        self._next = None

    def set_next(self, handler):
        """
        Set the next handler in the chain.

        :type handler: Handler
        :rtype: Handler
        """
        self._next = handler
        return handler

    def handle(self, request):
        """
        Try to handle the request, or pass it to the next handler.

        :type request: int
        :rtype: str or None
        """
        if self._next:
            return self._next.handle(request)
        return None


class ConcreteHandler(Handler):
    """
    A handler that handles a request if it matches
    the handler's level.
    """
    def __init__(self, level):
        super().__init__()
        self._level = level

    def handle(self, request):
        if request == self._level:
            return "Handler {} handled request {}".format(
                self._level, request
            )
        return super().handle(request)
