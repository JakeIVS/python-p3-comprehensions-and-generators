#!/usr/bin/env python3

def return_evens(num_list):
    pass
    evens_list = []
    for n in num_list:
        if not n % 2:
            evens_list.append(n)
    return evens_list

def make_exclamation(sentence_list):
    return [string + "!" for string in sentence_list]