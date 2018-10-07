product= {}
print("Create dictionary to save product and its respective area where it can be delivered")
product_count = int(input('how many product do you want to add in DB'))

for i in range(product_count):
    product_name = input('Enter product name: ')
    product_available_in_city = list(input('Enter the city list: ').split(','))
    product[product_name] = product_available_in_city
print(product)

product_needed = input('enter the product name you want to buy: ')
if product_needed in product:
    product_needed_in_city = input('enter your city name: ')
    product_available_in_city = product[product_needed]
    if product_available_in_city  in product_available_in_city:
        print('Yay! this product is available in your{}'.format(product_needed_in_city))
    else:
        print('Sorry! this product is not available in {} area. we are arriving soon :)'.format(product_needed_in_city))

