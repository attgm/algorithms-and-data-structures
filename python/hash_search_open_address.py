#! /usr/bin/env python3
from enum import Enum

HASH_SIZE: int = 190979
HASH_COEFF: int = 67

class Marker(Enum):
    EMPTY = "empty"
    DELETED = "deleted"



def hash_func(key:int) -> int:
    return (key * HASH_COEFF) % HASH_SIZE

def insert(hash_table: list[int|Marker], key:int) -> bool:
    index : int = hash_func(key)
    insert_index : int | None = None

    for _ in range(HASH_SIZE):
        match hash_table[index]:
            case value if value == key:
                return True
            case Marker.EMPTY:
                if insert_index is None:
                    insert_index = index
                break
            case Marker.DELETED:
                if insert_index is None:
                    insert_index = index
        index = (index + 1) % HASH_SIZE

    if insert_index is None:
        return False
    else:
        hash_table[insert_index] = key
        return True
    
def search(hash_table: list[int|Marker], key:int) -> bool:
    index : int = hash_func(key)

    for _ in range(HASH_SIZE):
        match hash_table[index]:
            case value if value == key:
                return True
            case Marker.EMPTY:
                return False
        index = (index + 1) % HASH_SIZE
    return False


def remove(hash_table: list[int|Marker], key:int) -> bool:
    index : int = hash_func(key)
    
    for _ in range(HASH_SIZE):
        match hash_table[index]:
            case value if value == key:
                hash_table[index] = Marker.DELETED
                return True
            case Marker.EMPTY:
                return False
        index = (index + 1) % HASH_SIZE
    return False
    
def main():
    hash_table: list[int | Marker] = [Marker.EMPTY for _ in range(HASH_SIZE)]

    # These keys have the same hash value, so insertion uses linear probing.
    keys = [10, 10 + HASH_SIZE, 10 + 2 * HASH_SIZE]
    for key in keys:
        print(f"Hash of {key}: {hash_func(key)}")
        print(f"Insert {key}: {insert(hash_table, key)}")

    start = hash_func(keys[0])
    print("Slots after insertion:")
    for offset in range(len(keys)):
        index = (start + offset) % HASH_SIZE
        print(f"  Slot {index}: {hash_table[index]}")

    # Search for existing and missing keys.
    for key in keys + [99]:
        print(f"Search for {key}: {search(hash_table, key)}")

    # A deleted marker lets searches continue to later colliding keys.
    print(f"Remove {keys[0]}: {remove(hash_table, keys[0])}")
    print(f"Slot {start} after removal: {hash_table[start]}")
    for key in keys:
        print(f"Search for {key} after removal: {search(hash_table, key)}")

    # Another colliding key reuses the deleted slot.
    new_key = 10 + 3 * HASH_SIZE
    print(f"Insert {new_key}: {insert(hash_table, new_key)}")
    print(f"Slot {start} after reinsertion: {hash_table[start]}")
    print(f"Search for {new_key}: {search(hash_table, new_key)}")
    print(f"Remove missing key 99: {remove(hash_table, 99)}")

if __name__ == '__main__':
    main()
