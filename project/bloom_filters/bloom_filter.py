class BloomFilter:

    def __init__(self, filter_len):
        self.filter_len = filter_len
        self.bit_array = [0 for _ in range(filter_len)]

    def _base_hash_function(self, string, constant):
        result = 0

        for char in string:
            result = (result * constant + ord(char)) % self.filter_len
        return result

    def hash1(self, string):
        constant = 17
        return self._base_hash_function(string, constant)

    def hash2(self, string):
        constant = 223
        return self._base_hash_function(string, constant)

    def add(self, string):
        for index in [self.hash1(string), self.hash2(string)]:
            self.bit_array[index] = 1

    def is_value(self, string):
        return bool(
            self.bit_array[self.hash1(string)]
            and self.bit_array[self.hash2(string)]
        )
