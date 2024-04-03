import collections
import operator


def tallest_people(**kwargs):
    sorted_dict = dict(sorted(kwargs.items(), key=operator.itemgetter(0)))
    for key, value in sorted_dict.items():
        if value == max(sorted_dict.values()):
            print(f'{key} : {value}')

