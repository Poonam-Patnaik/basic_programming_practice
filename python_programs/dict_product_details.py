product_details = {}
product = {}
product_num = int(input('How many product you want to add : '))

def  get_product_details():
    product_name = input('Enter product name: ')
    prd_price = input('Enter product price: ')
    COD = (input('Enter product COD applicable or not : '))
    prd_seller = input('Enter product seller: ')
    return product_name,prd_price,COD,prd_seller


def set_product_details(prd_name,prd_price,prd_cod,prd_seller):
    product_details['prd_name']= prd_name
    product_details['prd_price'] = prd_price
    product_details['COD'] = prd_cod
    product_details['prd_seller'] = prd_seller
    return product_details


for i in range(product_num):
    product_id = input('Enter the product ID')
    if product_id in product:
        print('Product already exists')
    else:
        print("let's enter product details")
        prd_name,prd_price,prd_cod,prd_seller = get_product_details()
        product[product_id] = set_product_details(prd_name,prd_price,prd_cod,prd_seller)

print(product)