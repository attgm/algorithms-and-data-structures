#! /usr/bin/env python3

def fib_recursive(n: int) -> int:
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_loop(n: int) -> int:
    if n == 0:
        return 0
    fib: list[int] = [0 for _ in range(0, n + 1)]
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 2] + fib[i - 1]
    return fib[n]


def main():
    f1 : int = fib_recursive(5)
    print(f"Fibonacci number : f(5) = {f1} (recursive)")
    f2 : int = fib_loop(5)
    print(f"Fibonacci number : f(5) = {f2} (loop)")
        
    f3 : int = fib_recursive(35)
    print(f"Fibonacci number : f(35) = {f3} (recursive)")
    f4 : int = fib_loop(35)
    print(f"Fibonacci number : f(35) = {f4} (loop)")

if __name__ == "__main__":
    main()
