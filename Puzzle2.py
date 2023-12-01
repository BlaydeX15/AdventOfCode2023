import sys
import re
calibtotal = int(0)

yn = input("Would you like to write a new file? Y/N")

if yn.lower() == 'y':
    print("Please paste the data here and then press Ctrl D ")
    data = sys.stdin.read()
    file1 = open('Puzzle1List.txt', 'w')
    file1.write(data)

else:
    print("Using Old File")

with open('Puzzle1List.txt', 'r') as f:
    for line in f:
        newline = line.replace('one', 'one1one').replace('two', 'two2two').replace('three', 'three3three').replace('four', 'four4four').replace('five', 'five5five').replace('six', 'six6six').replace('seven', 'seven7seven').replace('eight', 'eight8eight').replace('nine', 'nine9nine').replace('zero', 'zero0zero')
        firstdigit = int(re.findall(r'\d', newline)[0])
        lastdigit = int(re.findall(r'\d', newline)[-1])
        calibline = int(firstdigit*10 + lastdigit)
        print(calibline)
        calibtotal += calibline
print(calibtotal)