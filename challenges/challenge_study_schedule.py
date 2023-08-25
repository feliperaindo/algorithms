def check_time(time):
    return True if (type(time) is not int) else False


def check_list(list_to_check):
    return True if type(list_to_check) is not list else False


def check_tuple(tuple_to_check):
    if type(tuple_to_check) is not tuple:
        return True
    if len(tuple_to_check) != 2:
        return True
    return False


def check_tuple_values(tuple_to_check):
    for item in tuple_to_check:
        if type(item) is not int:
            return True
    return False


def study_schedule(permanence_period, target_time):
    if check_time(target_time) or check_list(permanence_period):
        return None
    index = 0
    counter = 0
    list_len = len(permanence_period)
    while index < list_len:
        if check_tuple(permanence_period[index]) or check_tuple_values(
            permanence_period[index]
        ):
            return None

        first, second = permanence_period[index]

        if first <= target_time <= second:
            counter += 1

        index += 1
    return counter
