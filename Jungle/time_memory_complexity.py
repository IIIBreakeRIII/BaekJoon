import timeit
import tracemalloc
import matplotlib.pyplot as plt

__all__ = [
    "measure_time",
    "measure_memory",
    "plot_results",
]

def measure_time(func, inputs, repeat=3, number=1):
    """
    Measure average execution time of `func` over various inputs.

    Args:
        func (callable): The function to measure. Should accept positional arguments.
        inputs (List[Tuple]): A list of argument tuples to pass to `func`.
        repeat (int): Number of times to repeat timing per input.
        number (int): Number of executions per timing measurement.

    Returns:
        List[Tuple[Tuple, float]]: A list of (args, avg_time_sec).
    """
    results = []
    for args in inputs:
        timer = timeit.Timer(lambda: func(*args))
        times = timer.repeat(repeat=repeat, number=number)
        avg_time = sum(times) / repeat
        results.append((args, avg_time))
    return results


def measure_memory(func, inputs):
    """
    Measure peak memory usage of `func` over various inputs.

    Args:
        func (callable): The function to measure. Should accept positional arguments.
        inputs (List[Tuple]): A list of argument tuples to pass to `func`.

    Returns:
        List[Tuple[Tuple, float]]: A list of (args, peak_memory_kb).
    """
    results = []
    for args in inputs:
        tracemalloc.start()
        func(*args)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        results.append((args, peak / 1024))
    return results


def plot_results(time_data, memory_data, xlabel="Input Size", time_label="Time (s)",
                 memory_label="Memory (KB)", title_prefix="Complexity Analysis"):
    """
    Plot time and memory measurements side by side.

    Args:
        time_data (List[Tuple[Tuple, float]]): Output of measure_time.
        memory_data (List[Tuple[Tuple, float]]): Output of measure_memory.
        xlabel (str): Label for the x-axis.
        time_label (str): Label for the time plot y-axis.
        memory_label (str): Label for the memory plot y-axis.
        title_prefix (str): Common title prefix for plots.
    """
    # Extract x and y values
    x_vals = [args[0] if len(args)==1 else args for args, _ in time_data]
    time_vals = [t for _, t in time_data]
    mem_vals = [m for _, m in memory_data]

    # Plot time complexity
    plt.figure()
    plt.plot(x_vals, time_vals, marker='o')
    plt.title(f"{title_prefix} - Time")
    plt.xlabel(xlabel)
    plt.ylabel(time_label)
    plt.grid(True)

    # Plot memory complexity
    plt.figure()
    plt.plot(x_vals, mem_vals, marker='o')
    plt.title(f"{title_prefix} - Memory")
    plt.xlabel(xlabel)
    plt.ylabel(memory_label)
    plt.grid(True)

    plt.show()

