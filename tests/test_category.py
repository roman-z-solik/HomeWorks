import pytest
from src.product import Product


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации, но и получение " "дополнительных функций для удобства жизни"
    )
    assert len(first_category.products) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert first_category.product_count == 1
    assert second_category.product_count == 1


def test_category_str(first_category, second_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 27 шт."
    assert str(second_category) == "Телевизоры, количество продуктов: 7 шт."


def test_middle_price(first_category, category_wo_products):
    assert first_category.middle_price() == 140333.33333333334
    assert category_wo_products.middle_price() == 0

def test_exceptions(capsys, first_category):
    assert first_category.product_count == 3
    add_product = Product("Xiaomi Redmi Note 11","1024GB, Синий", 31000.0, 14)
    first_category.add_product(add_product)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Количество товара Xiaomi Redmi Note 11 увеличено на 14 шт."
    assert message.out.strip().split("\n")[-1] == "Обработка товара прошла успешно."


def test_null(capsys, first_category):
    # add_product = Product("Xiaomi Redmi Note 11","1024GB, Синий", 31000.0, 0)
    # first_category.add_product(add_product)
    message = capsys.readouterr()
    print(message)
    with pytest.raises(ValueError):
        add_product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0)
        first_category.add_product(add_product)
    assert message.out.strip().split("\n")[-2] == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"
    assert message.out.strip().split("\n")[-1] == "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)"
