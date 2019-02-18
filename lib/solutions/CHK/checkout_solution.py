

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total_checkout = []
    item = {'A': 50, 'B': 30, 'C': 20, 'D': 15}


    #dealing with single items
    for sku in skus:
        if sku in item.keys():
            total_checkout.append(item[sku])

    return sum(total_checkout)


print(checkout('AA'))
print(checkout("BBB"))

