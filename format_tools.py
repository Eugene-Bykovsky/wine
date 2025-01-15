def get_year_word(years):
    last_digit = years % 10
    last_two_digits = years % 100

    if last_digit == 1 and last_two_digits != 11:
        return "год"
    elif 2 <= last_digit <= 4 and not (12 <= last_two_digits <= 14):
        return "года"
    else:
        return "лет"
