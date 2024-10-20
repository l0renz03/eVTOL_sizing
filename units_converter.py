# This file contains all the functions used for converting units.


def kg_N(value):
    """
    Convert kilograms to Newtons.
    Args:
        value: Value in kilograms

    Returns:
        Value in Newtons
    """
    return value * 9.81


def lbs_kg(value):
    """
    Convert pounds of mass to kilograms.
    Args:
        value: Value in pounds

    Returns:
        Value in kilograms
    """
    return value * 0.45359237


def kg_lbs(value):
    """
    Convert kilograms to pounds of mass.
    Args:
        value: Value in kilograms

    Returns:
        Value in pounds of mass
    """
    return value / 0.45359237


def in_m(value):
    """
    Convert inches to meters.
    Args:
        value: Value in inches

    Returns:
        Value in meters
    """
    return value * 2.54 / 100


def m_in(value):
    """
    Convert meters to inches.
    Args:
        value: Value in meters

    Returns:
        Value in inches
    """
    return value * 100 / 2.54


def ft_m(value):
    """
    Convert feet to meters.
    Args:
        value: Value in feet

    Returns:
        Value in meters
    """
    return 0.3048 * value


def kts_m_s(value):
    """
    Convert knots to meters per second.
    Args:
        value: Value in knots

    Returns:
        Value in meters per second
    """
    return value * 0.514444444
