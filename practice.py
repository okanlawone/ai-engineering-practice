products = ["hoodie", "t-shirt", "pants", "shoes"]

prices = {
     "hoodie" : 29.99,
     "t-shirt" : 19,
     "pants" : 25,
     "shoes" : 35
}

def print_inventory(products, prices, sale_threshold):
    on_sale= []
    for i, item in enumerate(products, start=1): 
        if prices[item] >= sale_threshold:
            on_sale.append(item)
            print (f"{i}. {item.title()}: ${prices[item]} - Sale")
        else:
            print(f"{i}. {item.title()}: ${prices[item]} ")

    return on_sale

on_sale = print_inventory(products, prices, 20)

for item in on_sale: 
    print (f"{item.title()} is on sale")