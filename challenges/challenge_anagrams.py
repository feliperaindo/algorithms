def is_anagram(first_str: str, second_str: str):
    first, second = to_lower_case(first_str), to_lower_case(second_str)
    same_len, first_len, second_len = check_same_len(first, second)
    first_dict = create_dict(first, first_len)
    second_dict = create_dict(second, second_len)

    if not same_len or not check_is_anagram(first_dict, second_dict):
        return (return_anagram(first_dict), return_anagram(second_dict), False)

    anagram_sorted = return_anagram(first_dict)
    return (anagram_sorted, anagram_sorted, True)


def to_lower_case(string: str) -> str:
    return string.lower()


def check_same_len(first: str, second: str):
    first_len, second_len = len(first), len(second)

    return (
        (False, first_len, second_len)
        if first_len == 0 and second_len == 0
        else (first_len == second_len, first_len, second_len)
    )


def create_dict(string: str, length: int) -> (dict, dict):
    letters = {}

    index = 0
    while index < length:
        if string[index] not in letters:
            letters[string[index]] = 0
        letters[string[index]] += 1
        index += 1

    return letters


def check_is_anagram(f_dict: dict, s_dict: dict) -> bool:
    for letter in f_dict:
        if letter not in s_dict or f_dict[letter] != s_dict[letter]:
            return False
    return True


def return_anagram(dict_to_trans: dict) -> str:
    sorted_anagram = sort_dict(list(dict_to_trans.items()))
    return list_to_string(sorted_anagram)


def sort_dict(to_sort: list) -> list:
    if len(to_sort) < 2:
        return to_sort

    pivot_key, pivot_value = to_sort[0]
    less = [(key, value) for key, value in to_sort[1:] if key <= pivot_key]
    greater = [(key, value) for key, value in to_sort[1:] if key > pivot_key]

    return sort_dict(less) + [(pivot_key, pivot_value)] + sort_dict(greater)


def list_to_string(list_to_trans: list) -> str:
    final_string = ""

    for letter, quantity in list_to_trans:
        final_string = f"{final_string}{letter * quantity}"

    return final_string
