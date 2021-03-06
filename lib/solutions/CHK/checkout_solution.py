

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total_checkout = 0
    occurrence_of_A = skus.count('A')
    occurrence_of_B = skus.count('B')
    occurrence_of_C = skus.count('C')
    occurrence_of_D = skus.count('D')

    if occurrence_of_A + occurrence_of_B + occurrence_of_C + occurrence_of_D != len(skus):
        return -1

    if occurrence_of_A % 3 == 0:
        total_checkout += 130 * occurrence_of_A/3

    elif (occurrence_of_A + 1) % 3 == 0:
        total_checkout += checkout((occurrence_of_A + 1)*'A')-30

    elif (occurrence_of_A - 1) % 3 == 0:
        total_checkout += checkout((occurrence_of_A-1)*'A') + 50

    if occurrence_of_B % 2 == 0:
        total_checkout += 45 * occurrence_of_B/2

    else:
        total_checkout += checkout((occurrence_of_B-1)*'B') + 30

    total_checkout += (occurrence_of_C * 20) + (occurrence_of_D * 15)

    return total_checkout
