# Cannot use these functions/methods:
    # len
    # list.pop
    # list.remove

class Stacky:

    def __init__(self, data_type):
        self.stack = []
        self.data_type = data_type
        self.size = 0

    def top(self):
        """ Returns the top element on the stack """
        if self.size == 0:
            return None
        return self.stack[-1]

    def push(self, item) -> None:
        """ Puts an item on the stack. Raises TypeError if the wrong type is given. """
        if not isinstance(item, self.data_type):
            raise TypeError(f"Invalid type provided, expected type {self.data_type} but got {type(item)}")

        self.stack.append(item)
        self.size += 1

    def pop(self):
        """ Takes the top item off the stack and returns it """
        if self.size == 0:
            return None

        item = self.stack[-1]
        self.stack = self.stack[:-1]
        self.size -= 1
        return item

    def length(self) -> int:
        """ Returns the length of the stack """
        return self.size

    def clear(self) -> None:
        """ Clears out all items from the stack """
        self.stack.clear()
        self.size = 0


def main():
    s = Stacky(data_type=str)

    print(f"None: {s.top()}")
    print(f"None: {s.pop()}")
    print(f"0: {s.length()}")

    s.push("str1")
    print(f"str1: {s.top()}")
    print(f"1: {s.length()}")

    try:
        s.push(3)
    except TypeError as e:
        print(e) # the exception string

    s.push("str2")
    s.push("str3")
    print(f"3: {s.length()}")

    print(f"str3: {s.top()}")

    print(f"str3: {s.pop()}")
    print(f"str2: {s.top()}")
    print(f"2: {s.length()}")

    s.clear()
    print(f"0: {s.length()}")


if __name__ == "__main__":
    main()
