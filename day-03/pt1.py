import re
f = open("input.txt", "r")

numbers_regex="\d+"
symbols_regex="[^\.|\d]"

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
            if (numbers_match.group() == '35'):
                print(str(row)+'-'+str(i))
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

all_coords = set()
def get_coords_from_symbol(row, col, line_length):
    if (row > 0):
        for i in range(max(0, col-1),min(line_length-1, col+1)+1):
            all_coords.add(str(row-1)+'-'+str(i))
    if (row < row_length -1):
        for i in range(max(0, col-1),min(line_length-1, col+1)+1):
            all_coords.add((str(row+1)+'-'+str(i)))
    if (col > 0):
        all_coords.add((str(row)+'-'+str(col-1)))
    if (col < row_length-1):
        all_coords.add((str(row)+'-'+str(col+1)))

print(symbols)


for symbol in symbols:
    row, col = symbol.values()
    get_coords_from_symbol(row, col, line_length)

print(all_coords)

total = 0
for part_number in part_numbers:

    for coord in part_number["coords"]:
        if coord in all_coords:
            print(coord)
            print(part_number["value"])
            total+=part_number["value"]
            break
    

print(total)
    # print(col)

f.close()

