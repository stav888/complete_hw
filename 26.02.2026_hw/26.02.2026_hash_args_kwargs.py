class AlwaysEqual:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 999

    def __eq__(self, other):
        return isinstance(other, AlwaysEqual)


class NeverEqual:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 999

    def __eq__(self, other):
        return False if isinstance(other, NeverEqual) else False


def has_duplicates(*args):
    return len(args) != len(set(args))


def find_duplicates(*args):
    seen = set()
    duplicates = set()
    for value in args:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def pick_keys(prefix="is_", **kwargs):
    return {key: value for key, value in kwargs.items() if key.startswith(prefix)}
