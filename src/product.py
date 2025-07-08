from src.baseproduct import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """ Класс Product обладает следующими свойствами: Название (name), описание (description), цена (price), количество в наличии (quantity). """
    name: str
    description: str
    price: float
    quantity: int


    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self._current_product = 0
        super().__init__()
        self._current_product = 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная.")
            return

        if new_price < self._price:
            confirm = input(f'Цена снижается с {self._price:.2f} до {new_price:.2f}. Подтверждаете изменение (Y/N)? ')
            if not (confirm.lower() in ('y', 'yes')):
                return

        self._price = new_price

    @classmethod
    def new_product(cls, parameters_list: dict):
        """Создает новый продукт на основе переданных параметров."""
        return cls(
            parameters_list['name'],
            parameters_list['description'],
            parameters_list['price'],
            parameters_list['quantity']
        )

    def __str__(self):
        return f'{self.name}, {self.price:.2f} руб., остаток: {self.quantity} шт.'

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError('Можно складывать только объекты типа Product')