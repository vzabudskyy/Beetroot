from random import randint

FIELD_SIZE = 8
MINES_COUNT = 1
FLAGS_COUNT = 8
RULES = """
        Hello, dear User!
        
        Please, follow this the rules below:
        
          Your input should be similar to this '1 1' or '1 1 F',
          if you want to put the flag on specified tile. First number
          describes row, second number describes column of the field. 
          By typing 'F' after coordinates you put the flag on the specified
          tile. Notice, that you can put the flag on closed tile only.
          If you open tile, which covers mine - you lose. If you want to
          win - you should to mark all mines by flags. The number on the 
          field will help you to do this(they describes amount of mines in
          one-tile range).
          
        Good luck and remember:
        DON'T REPEAT THIS IS YOUR REAL LIFE
        
        Have a nice day! 
        """


def prepare_game_field(field_size):
    """
    Field is a dict, where the keys is coordinates of tiles,
    and values is list, where 0-position element indicates mine
    or ground, and 1-position element is a cover layer(grass or
    field, that will be shown to user)/
    """
    field = {(x, y): ["G", "#"] for x in range(1, field_size+1) for y in range(1, field_size+1)}
    flags_list = []

    for i in range(MINES_COUNT):  # generating and planting mines
        field[(randint(1, 8), randint(1, 8))][0] = "M"
    mines = [key for key, value in field.items() if value[0] == "M"]  # list of mines will make our life easier

    return field, mines, flags_list


def show_field(field, content=None):
    if content == 0:
        for i in field:
            if i[1] == 8:
                print(i, "\n")
            else:
                print(i, end=" ")

    elif content == 1:
        for i in field:
            if i[1] == 8:
                print(field[i][0], "\n")
            else:
                print(field[i][0], end="    ")

    else:
        for i in field:
            if i[1] == 8:
                print(field[i][1], "\n")
            else:
                print(field[i][1], end="    ")


def nearest_neighbours(coordinates, mines):
    x, y = coordinates[0], coordinates[1]
    amount = 0
    for i in mines:
        if 0 <= abs(x - i[0]) <= 1 and 0 <= abs(y - i[1]) <= 1:
            amount += 1
    if amount == 0:
        count = " "
    else:
        count = str(amount)
    return count


def get_coordinates(field):
    while True:
        coordinates = input("Enter the coordinates or, if you like, set the flag: ").split(" ")
        if len(coordinates) == 3 and coordinates[1] == "F":
            flag = True
        else:
            flag = False

        if coordinates[0].isdigit() and coordinates[1].isdigit():
            coordinates = (int(coordinates[0]), int(coordinates[1]))

        if coordinates in field:
            break
        else:
            print("Incorrect input")
    return coordinates, flag


def put_flag(coordinates, flags, field):
    if coordinates in field:
        if coordinates not in flags:
            flags.append(coordinates)
            return "F"
        elif coordinates in flags:
            flags.remove(coordinates)
            return "#"
    else:
        return " "


def open_area(coordinates, field, mines):
    open_tiles = [(coordinates[0] + x, coordinates[1] + y) for x in range(-1, 2) for y in range(-1, 2)]
    open_tiles = [i for i in open_tiles if i in field]
    result = list(set(open_tiles).difference(set(mines)))

    return result


def players_turn(field, mines, flags):
    if mines == flags:  # win check
        return 1

    coordinates, flag = get_coordinates(field)  # get coordinates and flag status

    if coordinates in field:
        if flag is True:  # if user want to put a flag on tile
            field[coordinates][1] = put_flag(coordinates, flags, field)
        elif field[coordinates][0] == "M":  # lose statement
            return 0
        elif field[coordinates][0] == "G":
            for i in open_area(coordinates, field, mines):
                field[i][1] = nearest_neighbours(i, mines)
            return
    else:  # if user enter incorrect input
        return -1


def main():
    game_field, mines_list, game_flags = prepare_game_field(FIELD_SIZE)
    print(RULES)
    show_field(game_field, content=1)
    show_field(game_field)
    while True:
        result = players_turn(game_field, mines_list, game_flags)
        if result == 1:
            print(f"\n YOU WIN \n")
            break
        elif result == 0:
            print(f"\n YOU LOSE \n")
            break
        show_field(game_field)


if __name__ == "__main__":
    main()
