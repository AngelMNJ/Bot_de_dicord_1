import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890}{¡'¿][ñ,._~|ç><"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password