#! /usr/bin/env python3

def binary_search(data: list[int], value:int) -> int | None:
    lo : int = 0
    hi : int = len(data)

    while lo < hi:
        mid : int = (lo + hi) // 2
        if data[mid] == value:
            return mid
        elif data[mid] > value:
            hi = mid
        else:
            lo = mid + 1

    return None




def main():
    data: list[int] = [3, 8, 12, 17, 23, 31, 42]
    print(f"Target: {data}")

    for value in [17, 3, 42, 20]:
        index: int | None = binary_search(data, value)

        if index is None:
            print(f"{value}: Not found")
        else:
            print(f"{value}: index {index}")
    
if __name__ == "__main__":
    main()
