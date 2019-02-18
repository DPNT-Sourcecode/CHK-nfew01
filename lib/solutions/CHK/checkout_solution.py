

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # total_checkout = []
    # item = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    # item_special_offers = {'3A': 130, '2B': 45, '2C': 30, '2D': 25}
    #
    #
    # #dealing with single items
    # for sku in skus:
    #     if sku in item.keys():
    #         total.append(item[sku])
    #
    # #dealing with special offers
    #

    for sku in skus:
        if sku.startswith('3'):
            

print(checkout('A,B,C,D'))