#! /usr/bin/env python3
HASH_SIZE: int = 190979
HASH_COEFF: int = 67

def hash_func(key:int) -> int:
    return (key * HASH_COEFF) % HASH_SIZE

def search(hash_table: list[int|None], key:int) -> bool:
    hash_value : int = hash_func(key)
    if hash_table[hash_value] == key:
        return True
    else:
        return False   

def insert(hash_table: list[int|None], key:int) -> bool:
    hash_value : int = hash_func(key)
    if hash_table[hash_value] is None:
        hash_table[hash_value] = key
        return True
    else:
        return False

def remove(hash_table: list[int|None], key:int) -> bool:
    hash_value : int = hash_func(key)
    if hash_table[hash_value] == key:
        hash_table[hash_value] = None
        return True
    else:
        return False
    
def main():
    hash_table: list[int | None] = [None for _ in range(HASH_SIZE)]

    for key in [10, 20, 30]:
        print(f"Insert {key}: {insert(hash_table, key)}")

    # Search for existing and missing keys.
    for key in [10, 30, 99]:
        print(f"Search for {key}: {search(hash_table, key)}")

    # Keys separated by HASH_SIZE have the same hash value.
    # This implementation cannot insert a key into an occupied slot.
    colliding_key = 10 + HASH_SIZE
    print(f"Hash of 10: {hash_func(10)}")
    print(f"Hash of {colliding_key}: {hash_func(colliding_key)}")
    print(f"Insert colliding key {colliding_key}: {insert(hash_table, colliding_key)}")
    print(f"Search for {colliding_key}: {search(hash_table, colliding_key)}")

    # Removing the original key frees the slot for the colliding key.
    print(f"Remove 10: {remove(hash_table, 10)}")
    print(f"Search for 10 after removal: {search(hash_table, 10)}")
    print(f"Insert {colliding_key} after removal: {insert(hash_table, colliding_key)}")
    print(f"Search for {colliding_key}: {search(hash_table, colliding_key)}")
    print(f"Remove missing key 99: {remove(hash_table, 99)}")


if __name__ == '__main__':
    main()
