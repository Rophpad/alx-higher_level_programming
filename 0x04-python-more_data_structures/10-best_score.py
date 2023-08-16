#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or a_dictionary == {}:
        return None
    _max = 0
    for k in a_dictionary:
        if a_dictionary[k] > _max:
            _max = a_dictionary[k]
            the_key = k
    return the_key
