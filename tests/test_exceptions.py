import pytest

from src.product import Product


def test_exceptions(capsys, first_category):
    assert first_category.product_count == 3
    add_product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    first_category.add_product(add_product)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Количество товара Xiaomi Redmi Note 11 увеличено на 14 шт."
    assert message.out.strip().split("\n")[-1] == "Обработка товара прошла успешно."


def test_null(capsys, first_category):
    message = capsys.readouterr()
    with pytest.raises(ValueError):
        add_product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0)
        first_category.add_product(add_product)
    assert message.out.strip().split("\n")[-2] == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"
    assert message.out.strip().split("\n")[-1] == "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)"
