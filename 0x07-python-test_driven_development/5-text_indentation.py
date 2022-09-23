#!/usr/bin/python3
""" Module to add blank line after some characters"""


def text_indentation(text):
    """Indent giving text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    _t = text.replace(". ", ".").replace(".", ".\n\n")
    _t = _t.replace("? ", "?").replace("?", "?\n\n")
    _t = _t.replace(": ", ":").replace(":", ":\n\n")

    print(_t)
