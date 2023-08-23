def two_numbers_are_positive(a, b, c):
    positives = 0
    for n in [a, b, c]:
        if n > 0:
            positives += 1

    return True if positives == 2 else False


print(two_numbers_are_positive(14, -3, -4))
# print(two_numbers_are_positive((2, 4, -3)))