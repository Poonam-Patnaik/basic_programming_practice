
get_str = list( input('enter a string: '))
get_char = input('enter char that you want to replace')
length = len(get_str)
count = 0

for ele in  range (length):

    if get_str[ele] == get_char and count == 0:

        count = 1

    elif get_str[ele] == get_char and count == 1:

        get_str[ele] = '$'

new_str = ''.join (get_str)

print (new_str)