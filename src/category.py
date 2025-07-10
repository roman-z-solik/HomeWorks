from src.product import Product
from src.exceptions import ZeroRuntimeProduct


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

    def __init__(self, name, description, products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count = len(self.__products) if products else 0


    @property
    def products(self):
        return self.__products

    def __str__(self):
        product_qty_count = 0
        for product in self.__products:
            product_qty_count = product.quantity + product_qty_count
            continue
        return f"{self.name}, количество продуктов: {product_qty_count} шт."

    def add_product(self, adding_product: Product):
        """ Добавляет новый товар в категорию либо увеличивает количество имеющегося товара.
        Объект класса Product, представляющий товар. """
        if isinstance(adding_product, Product):
            try:
                found_product = next((p for p in self.__products if p.name == adding_product.name), None)
                if found_product:
                    found_product.price = adding_product.price
                    found_product.quantity += adding_product.quantity
                    print(f"Количество товара {adding_product.name} увеличено на {adding_product.quantity} шт.")
                else:
                    self.__products.append(adding_product)
                    Category.product_count = len(self.__products)
                    print(f"Товар {adding_product.name} в количестве {adding_product.quantity} шт. добавлен")
            finally:
                print ("Обработка товара прошла успешно.")


    def middle_price(self) -> float | int:
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product3 = Product("Xiaomi Redmi Note 11","1024GB, Синий", 31000.0, 14)
    product4 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 170000.0, 4)

    category1 = Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получение дополнительных функций для удобства жизни",
        products=[product1, product2],
    )
    category2 = Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет "
        "вашим другом и помощником",
        products=[
            Product(
                name='55" QLED 4K',
                description="Фоновая подсветка",
                price=123000.0,
                quantity=7,
            )
        ],
    )

    print(category1.products)
    print(category1.product_count)
    category1.add_product(product3)
    category1.add_product(product4)

    print(category1)
    print(category1.products)
    print(category1.product_count)
    print(category1.category_count)
    # print(category1.middle_price())

    category_n = Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получение дополнительных функций для удобства жизни",
        )

    # print(category_n.middle_price())