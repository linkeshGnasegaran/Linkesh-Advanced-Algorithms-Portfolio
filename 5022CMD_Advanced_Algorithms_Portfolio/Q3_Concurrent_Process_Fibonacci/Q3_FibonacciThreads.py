import threading
import time


# Recursive Fibonacci function
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# Function used by each thread
def calculate_fibonacci(n, results, start_times, end_times):
    start_times.append(time.perf_counter_ns())

    result = fibonacci(n)

    end_times.append(time.perf_counter_ns())

    results[n] = result


# Multithreading experiment
def multithreading_experiment():
    print("\n=== MULTITHREADING EXPERIMENT ===")

    all_times = []

    for round_number in range(1, 11):
        results = {}
        start_times = []
        end_times = []

        thread1 = threading.Thread(
            target=calculate_fibonacci,
            args=(35, results, start_times, end_times)
        )

        thread2 = threading.Thread(
            target=calculate_fibonacci,
            args=(38, results, start_times, end_times)
        )

        thread3 = threading.Thread(
            target=calculate_fibonacci,
            args=(40, results, start_times, end_times)
        )

        thread1.start()
        thread2.start()
        thread3.start()

        thread1.join()
        thread2.join()
        thread3.join()

        total_time = max(end_times) - min(start_times)
        all_times.append(total_time)

        print(f"Round {round_number}: {total_time:,} ns")

    average_time = sum(all_times) / len(all_times)

    print("\nFibonacci Results:")
    print("Fibonacci(35) =", results[35])
    print("Fibonacci(38) =", results[38])
    print("Fibonacci(40) =", results[40])
    print(f"\nAverage Multithreading Time: {average_time:,.0f} ns")

    return average_time


# Sequential experiment without multithreading
def sequential_experiment():
    print("\n=== SEQUENTIAL EXPERIMENT ===")

    all_times = []

    for round_number in range(1, 11):
        start_time = time.perf_counter_ns()

        result35 = fibonacci(35)
        result38 = fibonacci(38)
        result40 = fibonacci(40)

        end_time = time.perf_counter_ns()

        total_time = end_time - start_time
        all_times.append(total_time)

        print(f"Round {round_number}: {total_time:,} ns")

    average_time = sum(all_times) / len(all_times)

    print("\nFibonacci Results:")
    print("Fibonacci(35) =", result35)
    print("Fibonacci(38) =", result38)
    print("Fibonacci(40) =", result40)
    print(f"\nAverage Sequential Time: {average_time:,.0f} ns")

    return average_time


# Main program
print("=== FIBONACCI MULTITHREADING VS SEQUENTIAL PROGRAM ===")
print("Calculating Fibonacci(35), Fibonacci(38), and Fibonacci(40)")
print("Please wait. The experiment runs 10 rounds for each method.")

multithreading_average = multithreading_experiment()
sequential_average = sequential_experiment()

print("\n=== FINAL COMPARISON ===")
print(f"Average Multithreading Time: {multithreading_average:,.0f} ns")
print(f"Average Sequential Time:      {sequential_average:,.0f} ns")

if multithreading_average < sequential_average:
    print("\nResult: Multithreading was faster.")
else:
    print("\nResult: Sequential execution was faster.")