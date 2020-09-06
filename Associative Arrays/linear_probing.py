class HashTable(object):

    def __init__(self):
        self.size = 10
        self.key_list = [] * self.size
        self.value_list = [] * self.size

    def hash_function(self, key):

        sum =0
        for pos in range(len(key)):
            sum += ord(key[pos])

        return sum%self.size

    def put(self, key, value):

        index = self.hash_function(key)

        while index is not None:

            if self.key_list[index] == key:
                self.value_list[index] = value
                return

            index = (index+1)% self.size

        self.key_list[index] = key
        self.value_list[index] = value


    def get(self):
        pass



if __name__ == "__main__":

    hash_table = HashTable()


