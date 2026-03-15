"""
Observer pattern.

Define a one-to-many dependency between objects so that when one object
changes state, all its dependents are notified and updated automatically.

https://en.wikipedia.org/wiki/Observer_pattern

Example:
    >>> subject = Subject()
    >>> observer = ConcreteObserver("obs1")
    >>> subject.attach(observer)
    >>> subject.notify("hello")
    >>> observer.received
    'hello'
"""


class Subject:
    """Observable subject that notifies attached observers."""
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """
        Attach an observer.

        :type observer: Observer
        """
        self._observers.append(observer)

    def detach(self, observer):
        """
        Detach an observer.

        :type observer: Observer
        """
        self._observers.remove(observer)

    def notify(self, message):
        """
        Notify all observers with the given message.

        :type message: str
        """
        for observer in self._observers:
            observer.update(message)


class Observer:
    """Base observer interface."""
    def update(self, message):
        raise NotImplementedError


class ConcreteObserver(Observer):
    """An observer that stores the last received message."""
    def __init__(self, name):
        self.name = name
        self.received = None

    def update(self, message):
        self.received = message
