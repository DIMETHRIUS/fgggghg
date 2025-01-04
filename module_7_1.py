class Product:
    name = ''
    weight = float
    category = ''

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category}')

class Shop:
    def __init__(self, __file_name = 'products.txt'):
        self.__file_name = __file_name

    def get_products(self):
        get_file = open('products.txt', 'r')
        name_prod = get_file.read()
        get_file.close()
        return name_prod
    def add(self, * products):
        for product in products:
            if str(product) not in self.get_products():
                file = open('products.txt', 'a')
                file.write(f'{str(product)}\n')
                file.close()
            elif product.name in products:
                print(f'Продукт {product} ужe был в магазине, его общий вес теперь равен {products}')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
s1.add(p1, p2, p3)
print(s1.get_products())