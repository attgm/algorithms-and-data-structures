#! /usr/bin/env python3

def quick_sort(data: list[int], left: int, right: int):
    if right - left <= 1:
        return
    pivot_index: int = partition(data, left, right)
    quick_sort(data, left, pivot_index)
    quick_sort(data, pivot_index + 1, right)

def median3(data: list[int], i: int, j: int, k: int) -> tuple[int, int]:
    x, y, z = data[i], data[j], data[k]

    if x <= y <= z or z <= y <= x:
        return y, j
    if y <= x <= z or z <= x <= y:
        return x, i
    return z, k

def partition(data: list[int], left:int, right:int) -> int:
    pivot, pivot_index = median3(
        data, left, right - 1, (left + right - 1) // 2
    )

    data[pivot_index], data[right - 1] = data[right - 1], data[pivot_index]
    pivot_index = right - 1
    right -= 1

    while left < right:
        while left < right and data[left] < pivot:
            left += 1
        while left < right and data[right - 1] >= pivot:
            right -= 1
        if left < right:
            data[left], data[right - 1] = data[right - 1], data[left]
    
    data[pivot_index], data[left] = data[left], data[pivot_index]
    return left


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
        quick_sort(data, 0, len(data))
        print(f"After:  {data}")
        print()


if __name__ == "__main__":
    main()
