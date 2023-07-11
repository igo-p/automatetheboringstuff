spam = ['apples', 'cats', 'bananas', 'tofu', 'cats']

for index,item in enumerate(spam):
    if index == len(spam)-1:
        print('and {0}'.format(item))
    else:
        print(item,end=', ')