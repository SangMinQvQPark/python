f = open('C:\\Users\\1\\Desktop\\buy_list.txt', 'rt', encoding='utf-8')
lines = f.readlines()

a = list(range(11)[1:])
b = list(map(str, a))

for number in b:
    print(number)
