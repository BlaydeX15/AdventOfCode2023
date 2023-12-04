import sys
import re

yn = input("Would you like to write a new file? Y/N")

if yn.lower() == 'y':
    print("Please paste the data here and then press Ctrl D ")
    data = sys.stdin.read()
    file1 = open('Puzzle3List.txt', 'w')
    file1.write(data)

else:
    print("Using Old File")

maxblue = 0
maxred = 0
maxgreen = 0
powertotal = 0

with open('Puzzle3List.txt', 'r') as f:
    for line in f:
        sections = re.split(r'[;:]', line)
        gamenumber = re.search(r'Game (\d+)', line)
        if gamenumber:
            gamenumber = int(gamenumber.group(1))
        for index, section in enumerate(sections, start=1):
            match = re.search(r'\b(\d+)\s*red\b', section)
            if match:
                matched_red = int(match.group(1))
                if matched_red > maxred:
                    maxred = matched_red
            match = re.search(r'\b(\d+)\s*green\b', section)
            if match:
                matched_green = int(match.group(1))
                if matched_green > maxgreen:
                    maxgreen = matched_green
            match = re.search(r'\b(\d+)\s*blue\b', section)
            if match:
                matched_blue = int(match.group(1))
                if matched_blue > maxblue:
                    maxblue = matched_blue
            linepower = maxblue*maxgreen*maxred
        maxblue = 0
        maxred = 0
        maxgreen = 0
        powertotal += linepower
print(powertotal)