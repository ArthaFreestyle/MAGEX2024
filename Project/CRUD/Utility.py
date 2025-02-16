import random
import string

def gen_random_string(length:str):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))