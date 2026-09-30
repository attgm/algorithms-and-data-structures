#! /usr/bin/env python3
from dataclasses import dataclass

@dataclass
class Stack:
    data: list[int]
    top: int = 0

def push(stack: Stack, value: int) -> bool:
    if stack.top >= len(stack.data):
        return False
    stack.data[stack.top] = value
    stack.top += 1
    return True

def pop(stack: Stack) -> int | None:
    if stack.top <= 0:
        return None
    stack.top -= 1
    value : int = stack.data[stack.top]
    return value

def main():
    stack = Stack([0] * 3)
    print(f"Stack capacity: {len(stack.data)}")

    # Fill the stack, then try to push one more value.
    for value in [10, 20, 30]:
        print(f"Push {value}: {push(stack, value)}")
    print(f"Push 40 onto a full stack: {push(stack, 40)}")

    # Last in, first out: values are popped in the order 30, 20, 10.
    print("Pop all values (last in, first out):")
    while stack.top > 0:
        print(f"Pop: {pop(stack)}")
    print(f"Pop from an empty stack: {pop(stack)}")

    # The stack can be used again after it becomes empty.
    print(f"Push 50 onto the empty stack: {push(stack, 50)}")
    print(f"Pop: {pop(stack)}")

if __name__ == "__main__":
    main()
