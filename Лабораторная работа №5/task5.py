from random import sample
import string


def get_random_password(n=8) -> str:
    parol_ = sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, n)
    return ''.join(parol_)


print(get_random_password())

