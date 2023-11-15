from itertools import filterfalse, count


class MultiKeyDict:
    class KeyError(KeyError): ...

    def __init__(self):
        self._keys = {}
        self._values = {}

    def __setitem__(self, key, item):
        index = self._gen_index()

        self._keys[key] = index
        self._values[index] = item

    def set_alias(self, key, alias):
        if not key in self._keys.keys():
            raise self.KeyError(f"Unknown key: {key}")

        self._keys[alias] = self._keys[key]

    def pairing(self, leader, assignable):
        if leader not in self._keys.keys():
            raise self.KeyError(f"Unknown leader: {leader}")
        elif assignable not in self._keys.keys():
            raise self.KeyError(f"Unknown assignable: {assignable}")

        index = self._keys[assignable]

        self._keys[assignable] = self._keys[leader]

        self._clear(index)

    def __getitem__(self, key):
        try:
            index = self._keys[key]
        except KeyError:
            raise self.KeyError(f"Unknown key: {key}")

        try:
            return self._values[index]
        except KeyError:
            raise RuntimeError(f"Mismatch of values was recorded")

    def __delitem__(self, key):
        if not key in self._keys:
            raise self.KeyError(f"Unknown key: {key}")

        self._clear(self._keys.pop(key))


    def __repr__(self):
        return str(dict(self))

    def __iter__(self):
        keys = {}
        values = {}

        for key, index in self._keys.items():
            value = self._values[index]

            if index in keys.keys():
                keys[index].append(key)
            else:
                keys[index] = [key]
                values[index] = value

        for key, value in values.items():
            yield tuple(keys[key]), values[key]

    def items(self):
        return tuple(self.__iter__())

    def keys(self):
        return tuple(self._keys.keys())

    def values(self):
        return tuple(self._values.values())

    def _gen_index(self):
        return next(filterfalse(set(self._keys.values()).__contains__, count(1)))

    def _clear(self, index):
        if not index in self._keys.values():
            try:
                del self._values[index]
            except KeyError:
                raise RuntimeError(f"Mismatch of values was recorded")