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

totalblue = 0
totalred = 0
totalgreen = 0
validtotal = 0

with open('Puzzle3List.txt', 'r') as f:
    for line in f:
        sections = re.split(r'[;:]', line)
        gamenumber = re.search(r'Game (\d+)', line)
        validline = 1
        if gamenumber:
            gamenumber = int(gamenumber.group(1))
        for index, section in enumerate(sections, start=1):
            match = re.search(r'\b(\d+)\s*red\b', section)
            if match:
                matched_red = int(match.group(1))
                totalred += matched_red
            match = re.search(r'\b(\d+)\s*green\b', section)
            if match:
                matched_green = int(match.group(1))
                totalgreen += matched_green
            match = re.search(r'\b(\d+)\s*blue\b', section)
            if match:
                matched_blue = int(match.group(1))
                totalblue += matched_blue
            if totalred <= 12 and totalgreen <= 13 and totalblue <= 14:
                pass
            else:
                validline = 0
            totalblue = 0
            totalred = 0
            totalgreen = 0
        if validline == 1:
            validtotal += gamenumber
            print("Game number", gamenumber, "is valid. Current value is ", validtotal)

print(validtotal)