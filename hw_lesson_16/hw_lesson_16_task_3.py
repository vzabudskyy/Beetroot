"""
Task 3

Product Store

Write a class Product that has three attributes:

type
name
price
Then create a class ProductStore, which will have some Products
and will operate with all products in the store.
All methods, in case they can’t perform its action,
should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class.
You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single
                       product with a predefined price
                       premium for your store(30 percent)

set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified
                                                            by input identifiers (type or name).
                                                            The discount must be specified in percentage

sell_product(product_name, amount) - removes a particular amount of products
                                     from the store if available, in other case raises an error.
                                     It also increments income if the sell_product method succeeds.

get_income() - returns amount of many earned by ProductStore instance.

get_all_products() - returns information about all available products in the store.

get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
```

class Product:

    pass

class ProductStore:

pass

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product(Food, 'Ramen, 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell(‘Ramen’, 10)

assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)

```
"""


class Product:
    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price

    def __call__(self):
        return self.name, self.type, self.price


class ProductStore:
    def __init__(self):
        self.storage = []
        self.income = 0

    def add(self, product, amount):
        if type(product) != Product or type(amount) != int:
            raise ValueError

        if [product.name, product.type] not in [[i["product"].name, i["product"].type] for i in self.storage]:
            self.storage.append({"product": product,
                                 "amount": amount,
                                 "discount": 1})
            return
        else:
            for i in self.storage:
                if i["product"].name == product.name and i["product"].type == product.type:
                    i["amount"] += amount
                    return

    def get_all_products(self):
        info = []
        for i in self.storage:
            name, type_, price = i["product"]()
            info.append({"name": name,
                         "type": type_,
                         "price": price,
                         "amount": i["amount"],
                         "discount": i["discount"] * 100})
        return info

    def set_discount(self, identifier, percent, identifier_type="name"):
        if type(identifier_type) == type(identifier) == str and type(percent) == int and 0 < percent < 100:
            if identifier_type == "name":
                for i in self.storage:
                    if i["product"].name == identifier:
                        i["discount"] = percent / 100
            elif identifier_type == "type":
                for i in self.storage:
                    if i["product"].type == identifier:
                        i["discount"] = percent / 100
            else:
                raise ValueError
        else:
            raise ValueError

    def sell_product(self, product_name, amount):
        if type(product_name) != str or type(amount) != int:
            raise ValueError
        for i in self.storage:
            if i["product"].name == product_name:
                i["amount"] -= amount
                self.income += amount * i["product"].price * i["discount"]

    def get_income(self):
        return self.income

    def get_product_info(self, product_name):
        if type(product_name) != str:
            raise ValueError
        result = None
        for i in self.storage:
            if i["product"].name == product_name:
                result = (i["product"].name, i["amount"])
        if result is None:
            raise ValueError
        return result


if __name__ == "__main__":
    p = Product('Sport', 'Football T-Shirt', 100)

    p2 = Product('Food', 'Ramen', 1.5)

    s = ProductStore()

    s.add(p, 10)

    s.add(p2, 300)

    s.set_discount('Football T-Shirt', 50)

    s.sell_product('Ramen', 10)

    s.sell_product('Football T-Shirt', 2)

    assert s.get_product_info('Ramen') == ('Ramen', 290)
    assert s.get_income() == 115

    print(s.get_all_products())
