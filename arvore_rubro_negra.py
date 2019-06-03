import time

from static.red_black_tree import RedBlackTree
from static.graphic import Plot

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
    bst.pretty_print()

    insert_before = time.time()
    bst.insert(70)
    insert_after = time.time()
    insert_time = insert_after - insert_before

    delete_before = time.time()
    bst.delete_node(70)
    delete_after = time.time()
    delete_time = delete_after - delete_before
    print("O tempo para inserir um elemento foi de {} milisegundos".format(insert_time))
    print("O tempo para deletar um elemento foi de {} milisegundos".format(delete_time))

    plot = Plot()
    plot.compare_graph(insert_time, delete_time)


