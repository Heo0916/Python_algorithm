
class Dick:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]
    
my_dick = Dick()
my_dick.put("test", 3)
print(my_dick.get("test"))