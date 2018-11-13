class BiohazardException(Exception):
    """ Base exception for future application specific exceptions. """
    pass


class ContentDataException(BiohazardException):
    """ The content data is invalid. """
    pass
