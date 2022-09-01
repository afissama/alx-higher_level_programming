#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) is dict:
        n_dict = dict(sorted(a_dictionary.items(), key=lambda item: item[1]))
        return list(n_dict.keys())[-1]
