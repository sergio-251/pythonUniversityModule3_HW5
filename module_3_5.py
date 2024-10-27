# Рекурсия

def get_multiplied_digits(number):
    str_number = str(int(''.join(sorted(str(number)))))
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str(str_number)[1:]))

print(get_multiplied_digits(40302))
print(get_multiplied_digits(12350001))
print(get_multiplied_digits(9235000))