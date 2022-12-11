# TODO решить с помощью list comprehension и распечатать егоlist
from pprint import pprint
list_ = [{'bin': bin(_), 'dec': _, 'hex': hex(_), 'oct': oct(_)}for _ in range(16)]
pprint(list_)

