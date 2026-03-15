"""
State pattern.

Allow an object to alter its behavior when its internal state changes.
The object will appear to change its class.

https://en.wikipedia.org/wiki/State_pattern

Example:
    >>> door = Door()
    >>> door.state_name()
    'closed'
    >>> door.open()
    >>> door.state_name()
    'opened'
"""


class State:
    """Base state interface."""
    def open(self, door):
        raise NotImplementedError

    def close(self, door):
        raise NotImplementedError

    def name(self):
        raise NotImplementedError


class OpenedState(State):
    """State representing an opened door."""
    def open(self, door):
        pass  # already open

    def close(self, door):
        door._state = ClosedState()

    def name(self):
        return "opened"


class ClosedState(State):
    """State representing a closed door."""
    def open(self, door):
        door._state = OpenedState()

    def close(self, door):
        pass  # already closed

    def name(self):
        return "closed"


class Door:
    """A door that can be opened and closed using the State pattern."""
    def __init__(self):
        self._state = ClosedState()

    def open(self):
        self._state.open(self)

    def close(self):
        self._state.close(self)

    def state_name(self):
        """
        Return the name of the current state.

        :rtype: str
        """
        return self._state.name()
