import re

# Example values for start_pos and end_pos
start_pos = 5
end_pos = 10

# Your input text with multiple lines
text = """......755.
...$.*....
.664**598."""

# Split the text into lines
lines = text.split('\n')

# Search for the pattern with an asterisk in each line
for line_number, line in enumerate(lines, start=1):
    matches = re.findall(r'\d+', line)
    if matches:
        for match in matches:
            start_pos = max(line.find(match) - 1, 0)
            end_pos = line.find(match) + len(match) + 1
            match2 = re.search(f'.{{{start_pos},{end_pos}}}[*]', line)
            if match2:
                print(f"mid {match}")
            if line_number > 1:
                match2 = re.search(f'.{{{start_pos},{end_pos}}}[*]', lines[line_number - 2])
                if match2:
                    print(f"up {match}")
            if line_number < len(lines):
                match2 = re.search(f'.{{{start_pos},{end_pos}}}[*]', lines[line_number])
                if match2:
                    print(f"low {match}")
