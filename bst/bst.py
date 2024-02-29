class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value: int) -> None:
        """ Inserts a new node into the tree, or does nothing if trying to add a node that's already in the tree """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node: TreeNode, value: int) -> None:
        """ Helper method for inserting into a BST """
        if value == node.value:
            return
        elif value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value: int) -> TreeNode:
        """ Returns the node with the value, or None if it isn't in the tree """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: TreeNode, value: int) -> TreeNode:
        """ Helper method for searching, it recursively finds the node with the value, or None if it isn't in the tree """
        if node is None or node.value == value:
            return node
        elif node.value > value:
            return self._search_recursive(node.left, value)
        elif node.value < value:
            return self._search_recursive(node.right, value)
    
    def traverse_in_order(self, node: TreeNode) -> None:
        """ Prints out the nodes in order (sorted) """
        if node is not None:
            self.traverse_in_order(node.left)
            print(node.value)
            self.traverse_in_order(node.right)
    
    def traverse_pre_order(self, node: TreeNode) -> None:
        """ Prints out the nodes in pre order, (self, left, right) """
        if node is not None:
            print(node.value)
            self.traverse_pre_order(node.left)
            self.traverse_pre_order(node.right)
    
    def traverse_post_order(self, node: TreeNode) -> None:
        """ Prints the nodes in post order (left, right, self) """
        if node is not None:
            self.traverse_pre_order(node.left)
            self.traverse_pre_order(node.right)
            print(node.value)