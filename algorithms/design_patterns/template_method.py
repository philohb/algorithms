"""
Template Method pattern.

Define the skeleton of an algorithm in an operation, deferring some steps
to subclasses. Template Method lets subclasses redefine certain steps of
an algorithm without changing the algorithm's structure.

https://en.wikipedia.org/wiki/Template_method_pattern

Example:
    >>> report = HTMLReport()
    >>> report.generate()
    '<html>Some data</html>'
    >>> report = TextReport()
    >>> report.generate()
    '*** Some data ***'
"""


class Report:
    """
    Base report class that defines the template method.
    Subclasses override the hook methods to customize behavior.
    """
    def generate(self):
        """Template method that defines the report generation algorithm."""
        return self.header() + self.body() + self.footer()

    def header(self):
        raise NotImplementedError

    def body(self):
        return "Some data"

    def footer(self):
        raise NotImplementedError


class HTMLReport(Report):
    """Generate an HTML report."""
    def header(self):
        return "<html>"

    def footer(self):
        return "</html>"


class TextReport(Report):
    """Generate a plain text report."""
    def header(self):
        return "*** "

    def footer(self):
        return " ***"
