def hash1(s: str) -> int:
    return 7

def hash2(s: str) -> int:
    return len(s)

def hash3(s: str) -> int:
    return ord(s[0])

def hash4(s: str) -> int:
    return ord(s[0]) + ord(s[1])

def hash5(s: str) -> int:
    total = 0
    for c in s:
        total += ord(c)
    return total

def hash6(s: str) -> int:
    total = 0
    for i, c in enumerate(s):
        total += ord(c) * (i+1)
    return total


def main():
    strings = ["abc", "def", "apple", "banana", "abc", "cba"]

    for s in strings:
        print(f"{s}: {hash6(s)}")


if __name__ == "__main__":
    main()
