f = open("input.txt", "r")

def parse_game(game_text):
    game_text=game_text.strip('\n')
    title, game_info = game_text.split(': ')
    game_num = int(title[5:])

    return {
        "game_num": game_num,
        "game_info": game_info
    }

def step_to_object(step):
    colors = step.split(", ")
    color_map={}
    for color in colors:
        value, color_name = color.split(" ") 
        color_map[color_name]=int(value)

    return color_map

def parse_game_steps(game_info):
    steps = game_info.split('; ')
    # print(steps)
    return list(map(step_to_object, steps))
    

total = 0
bag_contents = {
    "red": 12,
    "green": 13,
    "blue": 14
}

for game in f:
    parsed_game = parse_game(game)
    steps = parse_game_steps(parsed_game["game_info"])

    is_valid = True
    for step in steps:
        for key, value in step.items():
            if value > bag_contents[key]:
                is_valid = False

    # print(parsed_game["game_num"])
    # print(steps)
    # print(is_valid)

    if (is_valid):
        total+=parsed_game["game_num"]


print(total)

f.close()
