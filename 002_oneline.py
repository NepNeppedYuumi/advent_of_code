# part 1
print(sum(
    map(
        lambda x:int(x[0].split(' ')[-1]) if not any((True for col in x[1].replace(';', ',').split(', ') if [12, 13, 14][
            ['red', 'green', 'blue'].index(
                col.split(' ')[-1])] < int(col.split(' ')[0]
        )))else 0,
    map(
        lambda x: x.strip().split(': '), open('002.txt', 'r')
    ))))


print(sum(map(lambda x:int(x[0].split(' ')[-1]) if not any((True for col in x[1].replace(';', ',').split(', ') if [12, 13, 14][['red', 'green', 'blue'].index(col.split(' ')[-1])] < int(col.split(' ')[0])))else 0,map(lambda x: x.strip().split(': '), open('002.txt', 'r')))))
