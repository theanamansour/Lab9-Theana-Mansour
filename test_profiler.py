import time
import unittest
import memory_profiler

from profiler import (
    slow_function,
    fast_function,
    memory_intensive_function,
)


class TestProfiler(unittest.TestCase):
    def time_function(self, func):
        start = time.perf_counter()
        result = func()
        return time.perf_counter() - start, result

    def test_slow_function(self):
        duration, result = self.time_function(slow_function)
        print(f"\nslow_function: {duration:.4f} seconds")
        self.assertGreaterEqual(duration, 2)
        self.assertEqual(result, 333283335000)

    def test_fast_function(self):
        duration, result = self.time_function(fast_function)
        print(f"\nfast_function: {duration:.6f} seconds")
        self.assertLess(duration, 1)
        self.assertEqual(result, 328350)

    def test_memory_intensive_function(self):
        before = memory_profiler.memory_usage()[0]
        duration, result = self.time_function(memory_intensive_function)
        after = memory_profiler.memory_usage()[0]

        print(f"\nmemory_intensive_function: {duration:.4f} seconds")
        print(f"Memory before: {before:.2f} MiB")
        print(f"Memory after: {after:.2f} MiB")

        self.assertLess(duration, 5)
        n = 10000000
        self.assertEqual(result, n * (n - 1) * (2 * n - 1) // 6)


if __name__ == "__main__":
    unittest.main()