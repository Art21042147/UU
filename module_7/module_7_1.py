class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        if not self.file_exists():
            file = open(self.__file_name, 'w')
            file.close()

    def file_exists(self):
        try:
            file = open(self.__file_name, 'r')
            file.close()
            return True
        except FileNotFoundError:
            return False

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        existing_names = {line.split(', ')[0] for line in existing_products}

        file = open(self.__file_name, 'a')
        for product in products:
            if product.name in existing_names:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                file.write(str(product) + '\n')
                existing_names.add(product.name)
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
