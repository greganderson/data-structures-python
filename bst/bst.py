class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value: int) -> None:
        """ Inserts a new node into the tree, or does nothing if trying to add a node that's already in the tree """
        if self.root is None:
            self.root = Node(value)
            self.size += 1
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: Node, value: int) -> None:
        """ Helper method for inserting into a BST """
        if value == node.value:
            return
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
                self.size += 1
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                self.size += 1
            else:
                self._insert_recursive(node.right, value)

    def search(self, value: int) -> Node:
        """ Returns the node with the value, or None if it isn't in the tree """
        if self.root is None:
            return None

        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Node, value: int) -> Node:
        """ Helper method for searching, it recursively finds the node with the value, or None if it isn't in the tree """
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self._search_recursive(node.left, value)
        elif value > node.value:
            return self._search_recursive(node.right, value)

    def traverse_in_order(self, node: Node) -> None:
        """ Prints out the nodes in order (sorted) """
        if node is not None:
            self.traverse_in_order(node.left)
            print(node.value)
            self.traverse_in_order(node.right)

    def traverse_post_order(self, node: Node) -> None:
        """ Prints the nodes in post order (right, self, left) """
        if node is not None:
            self.traverse_post_order(node.right)
            print(node.value)
            self.traverse_post_order(node.left)

def main():
    bst = BST()

    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)

    for i in range(10000):
        bst.insert(i)

    print()
    print("*** In order ***")
    print()
    bst.traverse_in_order(bst.root)

    print()
    print("*** In reverse order ***")
    print()
    bst.traverse_post_order(bst.root)


if __name__ == "__main__":
    main()