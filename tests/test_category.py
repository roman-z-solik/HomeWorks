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
