#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) is dict:
        if (len(a_dictionary) > 0):
            items = a_dictionary.items()
            n_dict = dict(sorted(items, key=lambda item: item[1]))
            return list(n_dict.keys())[-1]
    return None
