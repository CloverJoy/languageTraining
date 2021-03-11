# snarter dictionary

class TagCloud:
    def __init__(self):
        # private member __tags
        self.tags = {}

    def add(self, tag):
        self.tags[tag] = self.tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
# get item

cloud["python"]
cloud.add("python")
cloud.add("python")
cloud.add("python")

print(cloud.tags)


class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = Product(10)
print(product.price)
