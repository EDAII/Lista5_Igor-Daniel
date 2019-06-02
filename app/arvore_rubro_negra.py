from static.red_black_tree import RedBlackTree

if __name__ == "__main__":
    bst = RedBlackTree()
    bst.insert(8)
    bst.insert(18)
    bst.insert(5)
    bst.insert(15)
    bst.insert(17)
    bst.insert(25)
    bst.insert(40)
    bst.insert(80)
    # bst.delete_node(25)
    bst.pretty_print()
