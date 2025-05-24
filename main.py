from __future__ import annotations
from functools import wraps
import python_rust_practice as prp
import time

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__}({args[0]}) took {end - start:.6f} seconds → result: {result}")
        return result
    return wrapper

@timed
def test_python(n: int):
    def fib_py(n: int) -> int:
        if n <= 1:
            return n
        return fib_py(n - 1) + fib_py(n - 2)
    return fib_py(n)

@timed
def test_rust(n: int):
    return prp.fib_rs(n)

def main():
    n = 40
    test_python(n)
    test_rust(n)

if __name__ == "__main__":
    main()
