def is_numbers_in_string(string_):
    state = False
    nums = []
    for i in string_:
        try:
            nums.append(int(i))
            state = True
            break
        except ValueError:
            pass
    return state
