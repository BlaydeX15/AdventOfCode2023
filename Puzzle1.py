import sys
import re
calibtotal = int(0)

yn=input("Would you like to write a new file? Y/N")

if yn.lower() == 'y':
    print("Please paste the data here and then press Ctrl D ")
    data = sys.stdin.read()
    file1 = open('Puzzle1List.txt', 'w')
    file1.write(data)

else:
    print("Using Old File")

with open('Puzzle1List.txt', 'r') as f:
    for line in f:
        firstdigit = int(re.findall(r'\d', line)[0])
        lastdigit = int(re.findall(r'\d', line)[-1])
        calibline = int(firstdigit*10 + lastdigit)
        print(calibline)
        calibtotal += calibline
print(calibtotal)

