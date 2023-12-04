import sys
import re

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
    match = re.search(r'\d+', line)
    if match:
        print(match)