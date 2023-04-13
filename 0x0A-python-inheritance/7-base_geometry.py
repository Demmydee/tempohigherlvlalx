#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Base geometry."""

    def area(self):
        """Public instance method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value validator.
        Args:
            name : Name of parameter.
            value : Parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
