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
    match = re.search(r'[^\w\s.]', line)
    if match:
        symbol_position = match.start()
        above_characters = lines[i - 1][symbol_position - 1:symbol_position + 1] if i > 0 else None
        line_characters = lines[i][symbol_position - 1:symbol_position + 1]
        below_characters = lines[i + 1][symbol_position - 1:symbol_position + 1] if i < len(lines) - 1 else None
        def extract_number(characters):
            if characters is not None:
                match = re.search(r'\b(\d+)\b', characters)
                return match.group(1) if match else None
            return None

        above_number = extract_number(above_characters)
        below_number = extract_number(below_characters)

        print("Above Numbers:", above_number)
        print("Line Numbers:", line_number)
        print("Below Numbers:", below_number)

# This is bad because i need to stop it from counting numbers nultiple times. Easier to just check each number and say yes or no.
