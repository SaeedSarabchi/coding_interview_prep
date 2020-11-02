def flip_bit_to_win(num):

    longest_run = 0
    current_run = 0
    last_run = 0
    no_zero = True
    while num > 0:
        digit = num & 1
        if digit == 1:
            current_run += 1
        else:
            no_zero = False
            if (current_run + last_run) > longest_run:
                longest_run = current_run + last_run
            last_run = current_run
            current_run = 0
        num = num >> 1

    if (current_run + last_run) > longest_run:
        longest_run = current_run + last_run

    if no_zero:
        return longest_run
    return longest_run + 1

print(flip_bit_to_win(0b111))
a = 0b111
