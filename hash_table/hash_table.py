class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.items: list[str] = [[] for i in range(self.size)]

    def add(self, item: str) -> None:
        item_hash = self.custom_hash(item)
        index = item_hash % self.size
        if item not in self.items[index]:
            self.items[index].append(item)

    def get_index(self, item: str) -> int:
        return self.custom_hash(item) % self.size

    def custom_hash(self, s: str) -> int:
        total = 0
        for i, c in enumerate(s):
            total += ord(c) * (i+1)
        return total

    def get_items(self) -> list[str]:
        result = []
        for sublist in self.items:
            for item in sublist:
                if item != "":
                    result.append(item)
        return result


def main():
    strings = ["abc", "def", "apple", "banana", "abc", "cba", "a"]

    ht = HashTable(size=3)
    for s in strings:
        ht.add(s)

    print(ht.get_items())


if __name__ == "__main__":
    main()