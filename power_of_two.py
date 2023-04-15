def power_of_two(input_number):
    current_number = 1
    while current_number <= input_number:
        if current_number == input_number:
            return True
        else:
            current_number *= 2
    return False