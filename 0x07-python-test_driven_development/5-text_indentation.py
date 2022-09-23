def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    _t = text.replace(". ", ".").replace(".", ".\n\n")
    _t = _t.replace("? ", "?").replace("?", "?\n\n")
    _t = _t.replace(": ", ":").replace(":", ":\n\n")

    print(_t)
