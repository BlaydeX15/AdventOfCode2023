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
        for match in matches:
            start_pos = max(line.find(match) - 1, 0)
            end_pos = line.find(match) + len(match) + 1
            print(start_pos, end_pos)
            match2 = re.search(f'.{{{start_pos},{end_pos}}}[*]', line)
            if match2:
                    print(f"mid {match}")
            if line_number > 1:
                match2 = re.search(f'.{{{start_pos},{end_pos}}}[*]', lines[line_number - 1])
                if match2:
                    print(f"up {match}")
            if line_number < len(lines):
                match2 = re.search(f'.{{{start_pos},{end_pos}}}[*]', lines[line_number + 1])
                if match2:
                    print(f"low {match}")

