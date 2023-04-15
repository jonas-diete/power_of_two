def power_of_two(number):
    start = 2
    while start <= number:
        if start == number:
            return True
        else:
            start *= 2
    return False