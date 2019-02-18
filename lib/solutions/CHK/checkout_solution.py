

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total_checkout = []
    item = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    item_special_offers = {'3A': 130, '2B': 45, '2C': 30, '2D': 25}


    #dealing with single items
    for sku in skus:
        if sku == item.keys():
            total_checkout.append(item[sku])

    #dealing with special offers

    for sku in skus:
        if sku == item_special_offers.keys():
            total_checkout.append(item[sku])

    return sum(total_checkout)

print(checkout('A,B,C,D'))
print(checkout('3A,2B'))
