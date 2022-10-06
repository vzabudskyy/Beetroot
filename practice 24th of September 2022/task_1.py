players = [
   "Igor",
   "Oleg",
   "Petr",
   "Foma",
   "Julya",
   "Ioan",
   "Matfey",
   "Maria",
   "Iuda",
]


def generate_schedule(players):
    length = len(players)
    schedule = [f"{i[0]} -- {i[1]}" for i in zip(players[:length//2], players[-1:-length//2-1:-1])]
    if length % 2 != 0:
        schedule.append(players[len(players)//2])
    return schedule


if __name__ == "__main__":
    print(generate_schedule(players))

