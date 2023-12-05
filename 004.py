from itertools import zip_longest

# part 1
totaal = 0
with open('004.txt', 'r') as file:
    for line in file:
        wins, owns = line.strip().split(": ")[1].split(" | ")
        wins = wins.split()
        owns = owns.split()
        same = sum((own in wins for own in owns if own != ''))
        totaal += int(2 ** (same - 1))
        """
            0 duplicates    2 ^ -1 = 0.5
            1 duplicate     2 ^ 0 = 1
            2 duplicates    2 ^ 1 = 2
            3 duplicates    2 ^ 2 = 4
            .....
        """
print(totaal)

# part 2
totaal = 0
duplicates = []
with open('004.txt', 'r') as file:
    for i, line in enumerate(file, start=1):
        wins, owns = line.strip().split(": ")[1].split(" | ")
        wins = wins.split()
        owns = owns.split()
        same = sum((own in wins for own in owns if own != ''))
        current_dupes = duplicates.pop(0) if len(duplicates) else 0
        duplicates = [(1 + current_dupes) * bool(dupe) + org_dupe
                      for dupe, org_dupe in zip_longest(range(1, same + 1), duplicates, fillvalue=0)]
        totaal += 1 + current_dupes
print(totaal)
