import time


def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def display_time(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print(f'Total time: {t2 - t1:.2f}s')
        return result
    return wrapper


@display_time
def count_prime_nums(max_num):
    inside_count = 0
    for i in range(2, max_num):
        if is_prime(i):
           inside_count += 1
    return inside_count


count = count_prime_nums(10000)
print(count)
