from src.product import Product


class Smartphone (Product):
    def __init__(self, name, description, price, quantity, efficiency):
        super().__init__(self, name, description, price, quantity)
        self.efficiency = efficiency


if __name__ == "__main__":
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 500)
    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)