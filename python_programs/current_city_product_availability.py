product_available_in_city = list(input('enter 5 city name where product is available ').split(','))
current_city = input('Enter your city name')
flag = 0
for cities in product_available_in_city:
    if current_city == cities:
        flag = 1
        break
    else:
        continue

if flag == 1:
    print('Hurray! your city is in your product delivery range')
else:
    print('We are sorry but we are still not in your city')