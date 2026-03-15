"""
Proxy pattern.

Provide a surrogate or placeholder for another object to control
access to it.

https://en.wikipedia.org/wiki/Proxy_pattern

Example:
    >>> real = RealSubject()
    >>> proxy = ProtectionProxy(real, "admin")
    >>> proxy.request("admin")
    'RealSubject: handling request'
    >>> proxy.request("guest")
    'Proxy: access denied'
"""


class RealSubject:
    """The real object that the proxy represents."""
    def request(self):
        return "RealSubject: handling request"


class ProtectionProxy:
    """
    A proxy that controls access to the RealSubject
    based on a password.
    """
    def __init__(self, subject, password):
        self._subject = subject
        self._password = password

    def request(self, password):
        """
        Forward the request if the password matches,
        otherwise deny access.

        :type password: str
        :rtype: str
        """
        if password == self._password:
            return self._subject.request()
        return "Proxy: access denied"
