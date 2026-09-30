#! /usr/bin/env python3
from dataclasses import dataclass

@dataclass
class Queue:
    data: list[int]
    head: int = 0
    tail: int = 0
    count: int = 0

def enqueue(queue: Queue, value: int) -> bool:
    n : int = len(queue.data)
    if queue.count >= n:
        return False
    queue.data[queue.tail] = value
    queue.tail = (queue.tail + 1) % n
    queue.count += 1
    return True

def dequeue(queue: Queue) -> int | None:
    n : int = len(queue.data)
    if queue.count <= 0:
        return None
    value : int = queue.data[queue.head]
    queue.head = (queue.head + 1) % n
    queue.count -= 1
    return value

def main():
    queue = Queue([0] * 3)
    print(f"Queue capacity: {len(queue.data)}")

    # Fill the queue, then try to enqueue one more value.
    for value in [10, 20, 30]:
        print(f"Enqueue {value}: {enqueue(queue, value)}")
    print(f"Enqueue 40 into a full queue: {enqueue(queue, 40)}")

    # Removing 10 frees a slot. The circular buffer reuses it for 40.
    print(f"Dequeue: {dequeue(queue)}")
    print(f"Enqueue 40 after freeing a slot: {enqueue(queue, 40)}")

    # First in, first out: the remaining values come out as 20, 30, 40.
    print("Dequeue all remaining values (first in, first out):")
    while queue.count > 0:
        print(f"Dequeue: {dequeue(queue)}")
    print(f"Dequeue from an empty queue: {dequeue(queue)}")

    # The queue can be used again after it becomes empty.
    print(f"Enqueue 50 into the empty queue: {enqueue(queue, 50)}")
    print(f"Dequeue: {dequeue(queue)}")

if __name__ == "__main__":
    main()
