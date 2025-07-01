from src.product import Product


class Lawngrass (Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

# if __name__ == "__main__":
#     grass1 = Lawngrass("LawnGrass1", "Lawngrass - this is lawngrass", 30000.0, 2, "Hungary", 500)
#     print(grass1)
#     print(grass1.name)
#     print(grass1.description)
#     print(grass1.price)
#     print(grass1.quantity)
#     print(grass1.country)
#     print(grass1.germination_period)