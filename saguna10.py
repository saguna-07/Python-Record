str = 'apple mango apple orange orange apple guava mango mango'
str = str.split()  # [“apple’, ‘mango ‘.........’]
str2 = []
for i in str:
    if i not in str2:
        str2.append(i)

for i in range(0, len(str2)):
    print('Frequency of', str2[i], 'is :', str.count(str2[i]))
