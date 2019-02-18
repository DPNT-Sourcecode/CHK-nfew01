

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total_checkout = []
    item = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

    #dealing with single items
    for sku in skus:
        if sku in item.keys():
            total.append(item[sku])

    #dealing with special offers
    


print(checkout('A,B,C,D'))