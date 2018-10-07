sample_string = input('enter string')

string_dict = {}

for ele in sample_string:
    if ele in string_dict:
       string_dict[ele] = string_dict[ele] + 1
    else:
        string_dict[ele] = 1
print (string_dict)

