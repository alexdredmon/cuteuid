import re

alphabet            = "abcdefghijklmnopqrstuvwxyz"
leet_alphabet       = "abcd3fgh1jklmnopqr57uvwxyz"
hex_leet_alphabet   = "abcd3f641  1  09  57      "

leet_translation = str.maketrans(alphabet, leet_alphabet)
hex_leet_translation = str.maketrans(alphabet, hex_leet_alphabet)

alpha_pattern = re.compile('[\W_]+')


def convert(text, charset):
    text = alpha_pattern.sub('', text.lower())
    return text.translate(charset)


def to_leet(text):
    return convert(text, leet_translation)


def to_hex_leet(text):
    return convert(text, hex_leet_translation)
