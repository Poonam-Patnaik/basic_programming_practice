#list_of_words = ['hello', 'mine', 'nitesh choudhury', 'raja', 'hacker', 'hacker earth', 'hacker']
list_len = int(input('Enter the list length : '))
list_of_words = []
for i in range(list_len):
    value = input('enter string')
    list_of_words.append(value)
print(list_of_words)
biggest_word = ''
count = 0

for ele in list_of_words:

    if len(ele) > len(biggest_word):
        biggest_word = ele

    elif len(ele) == len(biggest_word):
        count = count + 1

if list_len-1 ==0:
    print('list have only one element')
elif list_len-1 == count:
    print('all list element have same length ')
else:
    print(biggest_word)