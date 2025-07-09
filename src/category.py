from src.product import Product


class Category:
    """
    Класс Category обладает следующими свойствами:
        название (name),
        описание (description),
        список товаров категории (products).
    """

    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def products(self):
        return self.__products

    def __str__(self):
        product_count = 0
        for product in self.__products:
            product_count = product.quantity + product_count
            continue
        return f"{self.name}, количество продуктов: {product_count} шт."

    def add_product(self, adding_product: Product):
        if isinstance(adding_product, Product):
            presence: bool = False
            for output in self.__products:
                if adding_product.name == output.name:
                    output.price = adding_product.price
                    output.quantity = output.quantity + adding_product.quantity
                    presence = True
            if not presence:
                self.__products.append(adding_product)
                Category.product_count += 1
        else:
            raise TypeError

    def middle_price(self) -> float | int:
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product3 = Product("Xiaomi Redmi Note 11","1024GB, Синий", 31000.0, 14)

    category1 = Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получение дополнительных функций для удобства жизни",
        products=[product1, product2, product3],
    )

    print(category1)
    print(category1.middle_price())

    category_n = Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получение дополнительных функций для удобства жизни",
        products=[],
    )

    print(category_n.middle_price())