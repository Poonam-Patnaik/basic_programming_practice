cities_friend_lived = list(input('enter 10 city name where your friend lived').split(','))
product_available_in_city = list(input('enter 5 city name where product is available ').split(','))
product_not_available_in_cities = []
for city in cities_friend_lived:
    if city in product_available_in_city:
        continue
    else:
        product_not_available_in_cities.append(city)
print(product_not_available_in_cities)