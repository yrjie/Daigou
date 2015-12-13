import random
import string

def pkgen(cls):
    key_len = 8
    key_chars = string.ascii_uppercase+string.ascii_lowercase+string.digits
    key = ""
    while True:
        key = "".join(random.choice(key_chars) for _ in range(key_len))
        print(key)
        if not cls.objects.filter(key=key):
            break
    return key