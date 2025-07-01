from src.product import Product


class Smartphone (Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


# if __name__ == "__main__":
#     smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 500, "Samsung Galaxy S23 Ultra", "256GB", "Серый цвет")
#     print(smartphone1.name)
#     print(smartphone1.description)
#     print(smartphone1.price)
#     print(smartphone1.quantity)
#     print(smartphone1.efficiency)
#     print(smartphone1.model)
#     print(smartphone1.memory)
#     print(smartphone1.color)