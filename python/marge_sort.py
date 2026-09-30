#! /usr/bin/env python3

def merge_sort(data: list[int], left: int, right: int):
    if right - left <= 1:
        return
    mid: int = (left + right) // 2
    merge_sort(data, left, mid)
    merge_sort(data, mid, right)
    merge_list(data, left, mid, right)

def merge_list(data: list[int], left: int, mid: int, right: int):
    p : int = left
    q : int = mid

    working : list[int] = [0] * (right - left)
    s : int = 0
    
    while p < mid and q < right:
        if data[p] < data[q]:
            working[s] = data[p]
            p += 1
        else:
            working[s] = data[q]
            q += 1
        s += 1

    while p < mid:
        working[s] = data[p]
        s += 1
        p += 1
    
    while q < right:
        working[s] = data[q]
        s += 1
        q += 1
    
    data[left:right] = working


def main():
    examples = [
        ("Unsorted values", [38, 27, 43, 3, 9, 82, 10]),
        ("Duplicates and negative values", [5, -2, 8, 5, 0, -2]),
        ("Already sorted values", [1, 2, 3, 4, 5]),
        ("Reverse-sorted values", [5, 4, 3, 2, 1]),
        ("A single value", [42]),
        ("An empty list", []),
    ]

    for description, data in examples:
        print(description)
        print(f"Before: {data}")
        # Sort in place. The right boundary is exclusive.
        merge_sort(data, 0, len(data))
        print(f"After:  {data}")
        print()


if __name__ == "__main__":
    main()
