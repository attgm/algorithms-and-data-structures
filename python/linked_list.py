#! /usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    nextNode: Node | None = None
    
@dataclass
class LinkedList:
    head: Node | None = None
    tail: Node | None = None

def init_list(lst: LinkedList, value: int):
    new_node: Node = Node(value)
    lst.head = new_node
    lst.tail = new_node

def append(lst: LinkedList, value: int):
    if lst.tail is None:
        init_list(lst, value)
    else:
        new_node: Node = Node(value)
        lst.tail.nextNode = new_node
        lst.tail = new_node
    
def prepend(lst: LinkedList, value: int):
    if lst.head is None:
        init_list(lst, value)
    else:
        new_node : Node = Node(value)
        new_node.nextNode = lst.head
        lst.head = new_node

def pop_front(lst: LinkedList) -> int | None:
    if lst.head is None:
        return None

    target = lst.head
    lst.head = target.nextNode

    if lst.head is None:
        lst.tail = None

    return target.value        

def node_at(lst: LinkedList, index: int) -> Node | None:
    if index < 0:
        return None

    node : Node | None = lst.head
    for _ in range(index):
        if node is None:
            return None
        node = node.nextNode

    return node

def insert(lst: LinkedList, index: int, value: int) -> bool:
    if index == 0:
        prepend(lst, value)
        return True
    
    previous : Node | None = node_at(lst, index - 1)
    if previous is None:
        return False
    
    new_node: Node = Node(value)
    new_node.nextNode = previous.nextNode
    previous.nextNode = new_node
    
    if new_node.nextNode is None:
        lst.tail = new_node
    
    return True

def remove(lst: LinkedList, index: int, value: int) -> bool:
    if index == 0:
        return pop_front(lst) is not None

    previous : Node | None = node_at(lst, index - 1);
    if previous is None:
        return False

    target : Node | None = previous.nextNode
    if target is None:
        return False
    
    previous.nextNode = target.nextNode

    if target.nextNode is None:
        lst.tail = previous

    return True



def show_list(lst: LinkedList) -> None:
    values: list[str] = []
    node = lst.head
    while node is not None:
        values.append(str(node.value))
        node = node.nextNode
    print("List: " + " -> ".join(values + ["None"]))


def main():
    lst = LinkedList()

    print("Create an empty list")
    show_list(lst)

    for value in [20, 40]:
        append(lst, value)
        print(f"Append {value}")
        show_list(lst)

    prepend(lst, 10)
    print("Prepend 10")
    show_list(lst)

    # Indices start at zero. Insert 30 between 20 and 40.
    print(f"Insert 30 at index 2: {insert(lst, 2, 30)}")
    show_list(lst)

    # Look up an existing index and an out-of-range index.
    for index in [2, 9]:
        node = node_at(lst, index)
        if node is None:
            print(f"Node at index {index}: not found")
        else:
            print(f"Node at index {index}: {node.value}")

    print(f"Insert 99 at invalid index 9: {insert(lst, 9, 99)}")
    show_list(lst)

    # Remove a middle node, then the tail. Indices shift after removal.
    # The current remove() API requires value, but only uses index.
    for value in [30, 40]:
        print(f"Remove {value} at index 2: {remove(lst, 2, value)}")
        show_list(lst)

    # Remove the remaining nodes from the front, then try an empty list.
    while lst.head is not None:
        print(f"Pop front: {pop_front(lst)}")
        show_list(lst)
    print(f"Pop front from an empty list: {pop_front(lst)}")

    # The list can be used again after its last node is removed.
    append(lst, 50)
    print("Append 50 to the empty list")
    show_list(lst)


if __name__ == "__main__":
    main()
