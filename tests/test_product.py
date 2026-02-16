from src.product import Product


def test_product_init(product1):
    assert product1.name == "Iphone 15"
    assert product1.description == "512GB, Gray space"
    assert product1.price == 210000.0
    assert product1.quantity == 8


def test_product_create():
    test_product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    test_product.name = "Iphone 15"
    test_product.description = "512GB, Gray space"
    test_product.price = 210000.0
    test_product.quantity = 8


def test_product_update(capsys, product1):
    product1.price = 0
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная."


def test_product_str():
    test_product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    print(test_product)


def test_product_add(product1, product2):
    assert (product1 + product2) == 2580000.0
