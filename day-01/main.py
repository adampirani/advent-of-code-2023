import re
f = open("input.txt", "r")

total=0

regex_query="(?=(\d|one|two|three|four|five|six|seven|eight|nine))"

string_to_digit_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

for jumbled_value in f:
    all_nums = re.findall(regex_query, jumbled_value)

    print(all_nums)

    first = all_nums[0]
    if first in string_to_digit_dict:
        first = string_to_digit_dict[first]

    last = all_nums[-1]
    if last in string_to_digit_dict:
        last = string_to_digit_dict[last]
        
    print(first+last)

    total+=int(first+last)

print(total)
f.close()

