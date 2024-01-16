import re
f = open("input.txt", "r")

numbers_regex="\d+"
symbols_regex="[\*]"

row=0
part_numbers = []
symbols = []
line_length = 0
for engine_line in f:
    engine_line = engine_line.strip()
    if (line_length == 0):
        line_length = len(engine_line)

    numbers_matches = re.finditer(numbers_regex, engine_line)
    for numbers_match in numbers_matches:

        part_number = {
            "value": int(numbers_match.group()),
            "coords": []
        }
        for i in range(numbers_match.start(), numbers_match.end()):
            part_index = str(row)+'-'+str(i)
            part_number["coords"].append(part_index)
        part_numbers.append(part_number)

    symbols_matches = re.finditer(symbols_regex, engine_line)
    for symbols_match in symbols_matches:
        symbols.append({
            "row": row,
            "col": symbols_match.start()
        })

    row+=1

row_length = row
# print(row_length)
# print(line_length)

def get_coords_from_symbol(row, col, line_length):
    coords = set()
    if (row > 0):
        for i in range(max(0, col-1),min(line_length-1, col+1)+1):
            coords.add(str(row-1)+'-'+str(i))
    if (row < row_length -1):
        for i in range(max(0, col-1),min(line_length-1, col+1)+1):
            coords.add((str(row+1)+'-'+str(i)))
    if (col > 0):
        coords.add((str(row)+'-'+str(col-1)))
    if (col < row_length-1):
        coords.add((str(row)+'-'+str(col+1)))

    return coords

# print(symbols)

total=0

for symbol in symbols:
    row, col = symbol.values()
    gear_touching_coords = get_coords_from_symbol(row, col, line_length)

    touching_engine_parts = []
    # inefficient loop but gets it done
    # could find a way to check only the part numbers nearby
    for part_number in part_numbers:
        for part_coord in part_number["coords"]:
            if part_coord in gear_touching_coords:
                touching_engine_parts.append(part_number)
                break

    if len(touching_engine_parts) == 2:
        part1, part2 = touching_engine_parts
        total+= part1["value"]*part2["value"]

print(total)
    # print(col)

f.close()

