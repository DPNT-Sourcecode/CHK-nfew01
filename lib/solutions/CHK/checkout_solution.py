

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total_checkout = []
    item = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

    if not skus:
        return -1



    for sku in skus:
        if sku in item.keys():
            total_checkout.append(item[sku])
        else:
            return -1

    return sum(total_checkout)


print(checkout('AA'))
print(checkout("BBB"))
print(checkout("-"))
print(checkout(""))
print(checkout("AxA"))
print(checkout("ABCa"))



