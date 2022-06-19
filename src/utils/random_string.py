import string
from random import choice


def generate_random_string(output_len=6):
    letters = string.ascii_letters + string.digits
    return ''.join(choice(letters) for _ in range(output_len))

