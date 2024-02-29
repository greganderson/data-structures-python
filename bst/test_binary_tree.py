import pytest

from binary_tree import BinaryTree


@pytest.fixture
def bst() -> BinaryTree:
    bst = BinaryTree()

    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    return bst

def test_search_existing_node(bst):
    assert bst.search(5).value == 5
    assert bst.search(6).value == 6

def test_search_non_existing_node(bst):
    assert bst.search(1) is None
    assert bst.search(10) is None

def test_insert_new_node(bst):
    bst.insert(10)
    assert bst.search(10).value == 10

    bst.insert(-1)
    assert bst.search(-1).value == -1

def test_insert_existing_node(bst):
    bst.insert(3)
    assert bst.search(3).value == 3

    bst.insert(6)
    assert bst.search(6).value == 6

def test_bst_structure(bst):
    assert bst.root.value == 5
    assert bst.root.left.value == 3
    assert bst.root.right.value == 7
    assert bst.root.left.left.value == 2
    assert bst.root.left.right.value == 4
    assert bst.root.right.left.value == 6