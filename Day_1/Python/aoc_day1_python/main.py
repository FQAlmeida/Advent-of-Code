from pathlib import Path


INPUT_FILEPATH = Path("../input/input.txt")

max_dwarf_calories = current_dwarf_calories = 0

def get_input_lines():
    with INPUT_FILEPATH.open("r") as fd:
        for line in fd:
            yield line.strip()

lines = get_input_lines()
for line in lines:
    if line in ["\n", ""]:
        max_dwarf_calories = max(max_dwarf_calories, current_dwarf_calories)
        current_dwarf_calories = 0
        continue
    calories = int(line)
    current_dwarf_calories += calories
print(f"Calories: {max_dwarf_calories}")
