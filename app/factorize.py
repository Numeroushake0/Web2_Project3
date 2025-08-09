import time
from app.factorize import factorize_sync, factorize_parallel, factorize
from multiprocessing import cpu_count


def measure_time(func, *args):
    start = time.time()
    results = func(*args)
    end = time.time()
    return results, end - start


def test_factorize():
    numbers = (128, 255, 99999, 10651060)

    print(f"Кількість ядер CPU: {cpu_count()}")

    print("Синхронна версія:")
    res_sync, time_sync = measure_time(factorize_sync, *numbers)
    for n, factors in zip(numbers, res_sync):
        print(f"Фактори числа {n}: {factors}")
    print(f"Час виконання: {time_sync:.4f} секунд\n")

    print("Паралельна версія:")
    res_par, time_par = measure_time(factorize_parallel, *numbers)
    for n, factors in zip(numbers, res_par):
        print(f"Фактори числа {n}: {factors}")
    print(f"Час виконання: {time_par:.4f} секунд\n")

    a, b, c, d = factorize(*numbers)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158,
                 304316, 380395, 532553, 760790, 1065106, 1521580,
                 2130212, 2662765, 5325530, 10651060]
    print("Тести пройдені успішно!")


if __name__ == "__main__":
    test_factorize()
