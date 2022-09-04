from random import randint, choices


class Baza:
    name = "Smereka-1"

    def __init__(self, equipment):
        self.equipment = equipment.copy()  # instances of class
        self.rent_equipment = dict()

    def add_product(self, product):  # -> add new product to equipment. Inform
        self.equipment.append(product)
        return f"{product} added into stock"

    def fill_user_withproducts(self, user):
        for _ in range(3):
            random_equipment = self.equipment[randint(0, len(self.equipment) - 1)]
            if random_equipment.rest_price > 0:
                user.push_product(random_equipment)
                self.equipment.remove(random_equipment)

    def fill_user_withproducts_1(self, user):  # we wrote it only for fun
        working_equipment = [gear for gear in self.equipment if gear.rest_price > 0]
        for _ in range(3):
            random_equipment = working_equipment[randint(0, len(self.equipment) - 1)]
            user.push_product(random_equipment)

    def check_equipment(self):
        typed_eq = [type(i) for i in self.equipment]  # contains types of every instance in self.equipment
        return {equip.__name__: typed_eq.count(equip) for equip in set(typed_eq)}

    def __str__(self):
        return f"Base {self.name} contains {self.check_equipment()}"


class User:
    def __init__(self, name="noname"):
        self.name = name
        self._equipment = []

    def push_product(self, product):
        print(f"{str(product)} rent by {self.name}")
        self._equipment.append(product)

    def return_product(self, base):
        for i in self._equipment:
            print(f"{str(i)} rented by {self.name} returned to base {Baza.name}")
            base.add_product(i)
        self._equipment = []

    def equipment(self):
        return self._equipment

    def __str__(self):
        str_equipment = ", ".join([str(i) for i in self._equipment])
        return f"{self.name} [{str_equipment}]"


class Product:
    price = 0
    rest_price = 10
    risk = 0

    def wee(self):  # -> reduce rest_price by percent or if risk --> rest_price == 0
        if randint(0, 100) < self.risk:
            self.rest_price = 0
        else:
            self.rest_price -= 0.5


class Snowboard(Product):
    price = 2000
    risk = 10
    rest_price = price

    def __str__(self):
        return "Snowboard"


class Skies(Product):
    price = 1000
    risk = 20
    rest_price = price

    def __str__(self):
        return "Skies"


class Helmet(Product):
    price = 100
    risk = 5
    rest_price = price

    def __str__(self):
        return "Helmet"


class Sledges(Product):
    price = 300
    risk = 30
    rest_price = price

    def __str__(self):
        return "Sledges"


class Funiculer:
    __allow_sets = [{Snowboard, Helmet},
                    {Skies, Helmet},
                    {Sledges}]

    def check(self, user):
        user_eq = set(map(type, user.equipment()))
        for i in self.__allow_sets:
            if i.intersection(user_eq) == i:
                return True
        return False

    def wee(self, user):
        if self.check(user):
            print(f"{user.name} can use the funiculer. ")
            for product in user.equipment():
                product.wee()
        else:
            print(f"\n{user.name} cannot use the funiculer."
                  f"\nIt is necessary to take appropriate equipment:"
                  f"\n{self.__allow_sets}")


if __name__ == "__main__":
    u = User("Joe")  # create user Joe
    base_equipment = [obj() for obj in choices([Skies, Snowboard, Sledges, Helmet], k=15)]
    print(base_equipment)
    b = Baza(base_equipment)
    for _ in range(10):
        b.add_product(Snowboard())
    print(b)
    b.fill_user_withproducts_1(u)
    print(b)
    print(u)
    f = Funiculer()  # create funiculer
    f.wee(u)
    u.return_product(b)
    print(u)
    print(b)
