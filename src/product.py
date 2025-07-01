class Product:
    """
    Класс Product обладает следующими свойствами:
        название (name),
        описание (description),
        цена (price),
        количество в наличии (quantity)
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self._current_product = 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif new_price < self.__price:
            user_input = input("Новая цена ниже. Заменить цену?(Y): ")
            if user_input == "Y" or user_input == "y" or user_input == "Н" or user_input == "н":
                self.__price = new_price
            else:
                return
        self.__price = new_price

    @classmethod
    def new_product(cls, parameters_list: dict):
        product = Product
        product.name = parameters_list["name"]
        product.description = parameters_list["description"]
        product.price = parameters_list["price"]
        product.quantity = parameters_list["quantity"]
        return product

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError
