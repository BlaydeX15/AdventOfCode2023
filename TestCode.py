import re

totalblue = 0
totalred = 0
totalgreen = 0

with open('Puzzle3List.txt', 'r') as f:
    for line in f:
        sections = re.split(r'[;:]', line)
        gamenumber = re.search(r'Game (\d+)', line)
        if gamenumber:
            gamenumber = int(gamenumber.group(1))
        for index, section in enumerate(sections, start=1):
            match = re.search(r'\b(\d+)\s*red\b', section)
            if match:
                matched_blue = int(match.group(1))
                totalblue += matched_blue
            match = re.search(r'\b(\d+)\s*green\b', section)
            if match:
                matched_green = int(match.group(1))
                totalgreen += matched_green
            match = re.search(r'\b(\d+)\s*blue\b', section)
            if match:
                matched_red = int(match.group(1))
                totalred += matched_red
        if totalred <= 12 and totalgreen <= 13 and totalblue <= 15:
            print("Game", gamenumber, ":", totalblue, totalgreen, totalred)
        else:
            print("Game", gamenumber, ":", "Invalid Game")
        totalblue = 0
        totalred = 0
        totalgreen = 0