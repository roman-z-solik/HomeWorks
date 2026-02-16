import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str):
    fullpath = os.path.abspath(path)
    with open(fullpath, "r", encoding="UTF-8") as f:
        json_data = json.load(f)
    return json_data


def load_json_data(json_data):
    """
    Функция читает информацию из JSON файла. На вход получает путь к файлу с данными,
    возвращает словарь с данными из JSON файла."""
    new_categorys = []
    for category in json_data:
        new_products = []
        for prod in category["products"]:
            new_products.append(Product(**prod))
        category["products"] = new_products
        new_categorys.append(Category(**category))

    return new_categorys
