def power_of_two(number):
    start = 1
    while start <= number:
        if start == number:
            return True
        else:
            start *= 2
    return False