import time

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

def test_measure_time():
    def sample_function():
        time.sleep(1)

    result = measure_time(sample_function)
    print(f"Test 1: {'Passed' if 0.9 < result < 1.1 else 'Failed'}, Time: {result:.2f} seconds")

    def add_numbers(a, b):
        return a + b


test_measure_time()
