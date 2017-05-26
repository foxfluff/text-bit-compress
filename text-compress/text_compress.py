
from math import log2
from pprint import PrettyPrinter

_calc_bits = lambda decimal: round(log2(decimal + 1) + .5)

def gen_key(string):
    key = set()
    for char in string:
        key.add(char)
    key = list(key)
    key.sort()
    key = "".join(key)

    return key


def compress(string, key = ""):
    if key == "":
        key = gen_key(string)

    char_size = _calc_bits(len(key))
    result = ""
    buffer = 0
    buffer_size = 0

    for char in string:
        buffer <<= char_size
        index = key.find(char)
        buffer += index
        buffer_size += char_size

        if buffer_size >= 8:
            diff = buffer_size - 8
            result += chr(buffer >> diff)
            buffer &= 2 ** diff - 1
            buffer_size = diff

    if buffer_size > 0:
        diff = 8 - buffer_size
        result += chr((buffer << diff) + (2 ** diff - 1))

    return result


def extract(string, key):
    result = ""
    buffer = 0
    buffer_size = 0
    char_size = _calc_bits(len(key))
    for char in string:
        buffer <<= 8
        buffer += ord(char)
        buffer_size += 8

        while buffer_size >= char_size:
            diff = buffer_size - char_size
            index = buffer >> diff
            if index != 2 ** char_size - 1:
                result += key[index] # to account for padding
            buffer &= 2 ** diff - 1
            buffer_size -= char_size

    return result