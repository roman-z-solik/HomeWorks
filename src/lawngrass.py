from src.product import Product


class Lawngrass (Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is Lawngrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


if __name__ == "__main__":
    grass1 = Lawngrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = Lawngrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    # print(grass1)
    # print(grass1.name)
    # print(grass1.description)
    # print(grass1.price)
    # print(grass1.quantity)
    # print(grass1.country)
    # print(grass1.germination_period)
    print(grass1 + grass2)