#!/usr/bin/python3
""" defines class LockedClass where the only new
instance attribute allowed is first_name """


class LockedClass:
    """ empty LockedClass """
    __slots__ = ["first_name"]
