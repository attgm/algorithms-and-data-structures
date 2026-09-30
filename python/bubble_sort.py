#! /usr/bin/env python3

def bubble_sort(data: list[int]):
    n: int = len(data)

    for i in reversed(range(1, n)):
        for j in range(0, i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


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
        bubble_sort(data)
        print(f"After:  {data}")
        print()


if __name__ == "__main__":
    main()
