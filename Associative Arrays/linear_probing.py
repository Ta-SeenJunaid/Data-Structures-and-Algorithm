class HashTable(object):

    def __init__(self):
        self.size = 10
        self.key = []
        self.value = []

    def hash_function(self, key):

        sum =0
        for pos in range(len(key)):
            sum += ord(key[pos])

        return sum%self.size

    def get(self):
        pass

    def put(self):
        pass

if __name__ == "__main__":
    pass
