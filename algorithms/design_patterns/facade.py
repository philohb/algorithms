"""
Facade pattern.

Provide a unified interface to a set of interfaces in a subsystem.
Facade defines a higher-level interface that makes the subsystem
easier to use.

https://en.wikipedia.org/wiki/Facade_pattern

Example:
    >>> computer = ComputerFacade()
    >>> computer.start()
    'CPU started. Memory loaded. Disk reading.'
"""


class CPU:
    def start(self):
        return "CPU started"


class Memory:
    def load(self):
        return "Memory loaded"


class Disk:
    def read(self):
        return "Disk reading"


class ComputerFacade:
    """Facade that simplifies starting a computer."""
    def __init__(self):
        self._cpu = CPU()
        self._memory = Memory()
        self._disk = Disk()

    def start(self):
        """
        Start the computer by coordinating subsystem components.

        :rtype: str
        """
        return "{}. {}. {}.".format(
            self._cpu.start(),
            self._memory.load(),
            self._disk.read()
        )
