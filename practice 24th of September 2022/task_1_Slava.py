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

result = ['Igor -- Iuda',
          'Oleg -- Maria',
          'Petr -- Matfey',
          'Foma -- Ioan',
          'Julya']


def generate_schedule(players):
    schedule = list(zip(players[0:len(players)//2], players[-1:-len(players)//2:-1]))
    schedule = [f"{x[0]} -- {x[1]}" for x in schedule]
    if len(players) % 2 == 1:
        schedule.append(players[len(players)//2])
    return schedule


if __name__ == "__main__":
    print(generate_schedule(players))