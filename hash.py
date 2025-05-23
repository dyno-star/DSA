class HashTable:
    def __init__(self, size = 7):
        self.data_map= [None] * size
        
    def hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)
    
    def set_item(self,key, value):
        index = self.hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.hash(key)
        if self.data_map[index] is not None:
            for i  in self.data_map[index]:
                if pair[0] == key:
                    return pair[1]
        return None


my_hash_table = HashTable()
my_hash_table.set_item("grapes", 10000)
my_hash_table.set_item("apples", 20000)
my_hash_table.set_item("oranges", 30000)
my_hash_table.print_table()