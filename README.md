# Интернет магазин

Проект создает ядро для интернет-магазина.

## Технологии
[Python] (https://www.python.org/)  
![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)

## Использование
Открыть проект в PyCharm.  

**products.py** содержит 1 класс:

`Product`  
Класс Product обладает следующими свойствами:  
  название (name),  
  описание (description),  
  цена (price),  
  количество в наличии (quantity),  
  родительский класс BaseProduct, описанный в файле **base_product.py**,
  вторым наследует класс-миксин, описанный в файле **print_mixin**
  

**category.py** содержит 1 класс:

`Category`
Класс Category обладает следующими свойствами:  
  название (name),  
  описание (description),  
  список товаров категории (products)  

**smartphone.py** содержит 1 подкласс:  

`Smartphone` подкласс от класса `Product`  
Помимо имеющихся у класса Product свойств добавлены:  
  производительность (efficiency),  
  модель (model),  
  объем встроенной памяти (memory),  
  цвет (color).  

**lawngrass.py** содержит 1 подкласс:  

`Lawngrass` подкласс от класса `Product`  
Помимо имеющихся у класса Product свойств добавлены:   
  страна-производитель (country),     
  срок прорастания (germination_period),      
  цвет (color).  

**utils.py** содержит 2 функции:

`read_json`
Функция читает информацию из JSON файла

`load_json_data`
Функция читает информацию из JSON файла.
На вход получает путь к файлу с данными, возвращает
словарь с данными из JSON файла.

Папка `tests` содержит файлы для тестирования модулей:  
**test_products.py**
**test_category.py**
**test_smartphone**
**test_lawngrass**
**test_print_mixin**

### Требования
Для установки и запуска проекта, необходимы:
[Python](https://www.python.org/)
[PyCharm](https://www.jetbrains.com/pycharm/)

## Команда проекта
[Roman Z](roman-z@inbox.ru)