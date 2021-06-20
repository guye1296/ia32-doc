import itertools


class BitMask(object):
    def __init__(self, *fields):
        self._size = max(
            map(lambda f: f[0] + f[1], fields),
            default=0
        )

        self._bitmask = '0' * self._size

        for offset, width in fields:
            self._bitmask = \
                self._bitmask[:offset] +\
                '1' * width +\
                self._bitmask[offset+width:]

    def __int__(self):
        return int(self._bitmask[::-1], base=2)

    def __str__(self):
        return '0b' + self._bitmask[::-1]

    def __repr__(self):
        return str(self)

    def _to_binary_string(self, value):
        bin_str = '{0:b}'.format(value).zfill(self._size)
        # reverse so indexing will work OK
        return bin_str[::-1]

    @property
    def size(self):
        return self._size

    def validate(self, value):
        value_str = self._to_binary_string(value)
        invalid_bits = [
            index for
            index, (value_bit, mask_bit) in
            enumerate(itertools.zip_longest(value_str, self._bitmask, fillvalue='0')) if
            value_bit == '1' and mask_bit == '0'
        ]

        if 0 == len(invalid_bits):
            return True

        raise ValueError(
            "Invalid assignment: bit(s) {} must be 0!".format(invalid_bits)
        )

    def __contains__(self, item):
        try:
            return self.validate(item)
        except ValueError:
            return False
