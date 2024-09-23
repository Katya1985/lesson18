def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number)
    first = (int(str_number[0]))
    remaining_digits = int(str_number[1:])
    return first * get_multiplied_digits(remaining_digits)


result = get_multiplied_digits(40203)
print(result)
