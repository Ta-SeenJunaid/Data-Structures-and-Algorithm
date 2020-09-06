class HashTable(object):

    def __init__(self):
        self.size = 10
        self.key_list = [None] * self.size
        self.value_list = [None] * self.size

    def hash_function(self, key):

        sum = 0
        for pos in range(len(key)):
            sum += ord(key[pos])

        return sum % self.size

    def put(self, key, value):

        index = self.hash_function(key)
        while self.key_list[index] is not None:

            if self.key_list[index] == key:
                self.value_list[index] = value
                return

            index = (index + 1) % self.size

        self.key_list[index] = key
        self.value_list[index] = value

    def get(self, key):

        index = self.hash_function(key)

        if self.key_list[index] is not None:
            while self.key_list[index] is not None:
                if self.key_list[index] == key:
                    print("Key : {}".format(key))
                    print("Value : {}".format(self.value_list[index]))
                    print("Index : {}".format(index))
                    return

                index = (index + 1) % self.size

        print("The key '{}' does not exist".format(key))


if __name__ == "__main__":
    hash_table = HashTable()

    # "Desktop" & "Mobilee" will create collusion

    hash_table.put("Desktop", 40)
    hash_table.put("Laptop", 50)
    hash_table.put("Mobilee", 20)
    hash_table.put("Mouse", 100)

    hash_table.get("Laptop")
    hash_table.get("Mobile")
    hash_table.get("Mobilee")
    hash_table.get("Tab")
    hash_table.get("Desktop")
