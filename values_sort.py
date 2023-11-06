from random import shuffle


def values_list_from_file(filename):
    """Given a text file of values, return an array of values"""
    values = []

    file = open(filename)
    for line in file:
        value = line.strip().lower()
        values.append(value)

    return values


def values_sort(values_list):
    values_to_choose_from = values_list
    shuffle(values_to_choose_from)
    selected_values = []

    print(values_to_choose_from)
    # for value in values_to_choose_from:


VALUES = values_list_from_file("values.txt")

values_sort(VALUES)
