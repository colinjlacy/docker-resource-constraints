import os
import time
import multiprocessing


def worker_function():
    iterations = 0
    while iterations < 10000000:
        _ = 1 + 1
        iterations += 1


if __name__ == '__main__':
    start_time = time.time()
    multiplier_string = os.getenv("PROCESS_MULTIPLIER", 1)

    try:
        multiplier = int(multiplier_string)
    except (ValueError, TypeError):
        exit(f"Invalid process multiplier: {multiplier_string}")

    if multiplier == 0:
        num_processes = 1
        worker_function()
    else:
        num_processes = multiprocessing.cpu_count() * multiplier
        processes = []
        for i in range(num_processes):
            p = multiprocessing.Process(target=worker_function)
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"{elapsed_time} seconds for {num_processes} processes to make 10,000,000 calculations")
