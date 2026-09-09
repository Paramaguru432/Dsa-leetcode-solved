from collections import defaultdict, OrderedDict

class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0

        # key -> [value, frequency]
        self.cache = {}

        # frequency -> OrderedDict of keys
        self.freq = defaultdict(OrderedDict)

    def get(self, key):
        if key not in self.cache:
            return -1

        value, frequency = self.cache[key]

        # Remove from old frequency
        del self.freq[frequency][key]

        # If this was the minimum frequency
        if frequency == self.min_freq and not self.freq[frequency]:
            self.min_freq += 1

        # Increase frequency
        frequency += 1

        self.freq[frequency][key] = None
        self.cache[key] = [value, frequency]

        return value

    def put(self, key, value):
        if self.capacity == 0:
            return

        # Key already exists
        if key in self.cache:
            self.cache[key][0] = value
            self.get(key)
            return

        # Cache is full
        if len(self.cache) >= self.capacity:
            # Remove least frequently used key
            key_to_remove, _ = self.freq[self.min_freq].popitem(last=False)

            del self.cache[key_to_remove]

        # Add new key
        self.cache[key] = [value, 1]
        self.freq[1][key] = None

        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)