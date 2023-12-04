import sys
import re

line_number = 0

yn = input("Would you like to write a new file? Y/N ")

if yn.lower() == 'y':
    print("Please paste the data here and then press Ctrl D ")
    data = sys.stdin.read()
    with open('Puzzle5List.txt', 'w') as file1:
        file1.write(data)
else:
    print("Using Old File")

with open('Puzzle5List.txt', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    line_number += 1
    matches = re.findall(r'\d+', line)
    if matches:
        print("Line Number", line_number)
        for match in matches:
            print("Number", match, "StartPos", line.find(match), "EndPos", line.find(match) + len(match))
        #loook at span, sub 1 from y and length of num from x to check top left, repeat for mid and right, curr row and bottom row.
        #if we see a symbol in the surrounding chars, mark num as valid, add to total
        #left pos + len = right pos?
