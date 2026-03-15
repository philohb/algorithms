"""
Command pattern.

Encapsulate a request as an object, thereby letting you parameterize
clients with different requests, queue or log requests, and support
undoable operations.

https://en.wikipedia.org/wiki/Command_pattern

Example:
    >>> invoker = Invoker()
    >>> invoker.execute(PrintCommand("hello"))
    'hello'
    >>> invoker.undo()
    'Undo: hello'
"""


class Command:
    """Base command interface."""
    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError


class PrintCommand(Command):
    """A command that returns a message on execute and undo."""
    def __init__(self, message):
        self._message = message

    def execute(self):
        return self._message

    def undo(self):
        return "Undo: {}".format(self._message)


class Invoker:
    """Stores and executes commands, with undo support."""
    def __init__(self):
        self._history = []

    def execute(self, command):
        """
        Execute a command and add it to the history.

        :type command: Command
        :rtype: str
        """
        self._history.append(command)
        return command.execute()

    def undo(self):
        """
        Undo the last executed command.

        :rtype: str
        """
        if not self._history:
            return None
        command = self._history.pop()
        return command.undo()
