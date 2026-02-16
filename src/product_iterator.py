class ProductIterator:
    def __init__(self, category_obj):
        self.category = category_obj
        self._current_product = 0

    def __iter__(self):
        self.current_product = 0
        return self

    def __next__(self):
        if self._current_product < len(self.category.products):
            iter_product = self.category.products[self._current_product]
            self._current_product += 1
            return iter_product
        else:
            raise StopIteration
