#! /usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class TreeNode:
    value: int
    left: TreeNode | None = None
    right: TreeNode | None = None

@dataclass
class BinarySearchTree:
    root: TreeNode | None = None

def search(tree: BinarySearchTree, value: int) -> TreeNode | None:
    node: TreeNode | None = tree.root
    while node is not None:
        if node.value == value:
            return node
        elif node.value > value:
            node = node.left
        else:
            node = node.right
    return None

def insert(tree: BinarySearchTree , value: int):
    tree.root = insert_impl(tree.root, value)

def insert_impl(node: TreeNode | None, value: int) -> TreeNode:
    if node is None:
        return TreeNode(value)
    elif node.value == value:
        return node
    elif node.value > value:
        node.left = insert_impl(node.left, value)
        return node
    else:
        node.right = insert_impl(node.right, value)
        return node

def remove_impl(node: TreeNode | None, value: int) -> TreeNode | None:
    if node is None:
        return None
    elif node.value == value:
        if node.left is None and node.right is None:
            return None
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            max_value: int = search_max(node.left)
            node.left = remove_impl(node.left, max_value)
            node.value = max_value
            return node
    elif node.value > value:
        node.left = remove_impl(node.left, value)
        return node
    else:
        node.right = remove_impl(node.right, value)
        return node

def search_max(node: TreeNode) -> int:
    pos: TreeNode = node
    while pos.right is not None:
        pos = pos.right
    return pos.value

def remove(tree: BinarySearchTree, value: int):
    tree.root = remove_impl(tree.root, value)


def main():
    tree = BinarySearchTree()
    values = [20, 10, 30, 5, 15, 25, 35, 27]
    for value in values:
        insert(tree, value)
    print(f"Inserted values: {values}")

    # Search for the root, the smallest and largest values, and a missing value.
    for value in [20, 5, 35, 99]:
        node = search(tree, value)
        if node is None:
            print(f"Search for {value}: not found")
        else:
            print(f"Search for {value}: found {node.value}")

    # Demonstrate the three removal cases.
    for value, description in [
        (5, "a leaf"),
        (25, "a node with one child"),
        (20, "a node with two children (the root)"),
    ]:
        remove(tree, value)
        print(f"Removed {value}: {description}")
        print(f"Search for {value} after removal: {search(tree, value)}")

    remaining = [value for value in sorted(values) if search(tree, value) is not None]
    print(f"Remaining values (in ascending order): {remaining}")
    
if __name__ == "__main__":
    main()
