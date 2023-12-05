

# part 1
total_count = 0
with open('001.txt', 'r') as file:
    for line in file:
        line = [num for num in line if num.isdecimal()]
        number = int(line[0] + line[-1])
        print(number)
        total_count += number
print(total_count)


# part 2
with open('001.txt', 'r') as file:
    lines = []
    for line in file:
        line2 = ''
        line = line.replace('one', 'one1one')
        for i in range(0, len(line)):
            if line[i].isnumeric():
                line2 += line[i]
                continue
            for y, value in enumerate(('one','two','three','four',
                                       'five','six','seven','eight','nine'), start=1):
                if line[i:i + 5].startswith(value):
                    line2 += str(y)
                    break
        line = int(line2[0] + line2[-1])
        lines.append(line)
    print(sum(lines))