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
        pass
    
    def _insert_recursive(self, node: TreeNode, value: int) -> None:
        """ Helper method for inserting into a BST """
        pass
    
    def search(self, value: int) -> TreeNode:
        """ Returns the node with the value, or None if it isn't in the tree """
        pass

    def _search_recursive(self, node: TreeNode, value: int) -> TreeNode:
        """ Helper method for searching, it recursively finds the node with the value, or None if it isn't in the tree """
        pass
    
    def traverse_in_order(self, node: TreeNode) -> None:
        """ Prints out the nodes in order (sorted) """
        pass
    
    def traverse_pre_order(self, node: TreeNode) -> None:
        """ Prints out the nodes in pre order, (self, left, right) """
        pass
    
    def traverse_post_order(self, node: TreeNode) -> None:
        """ Prints the nodes in post order (left, right, self) """
        pass