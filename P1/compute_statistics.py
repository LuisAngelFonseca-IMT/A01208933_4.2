"""
Module for computing descriptive statistics (mean, median, mode, standard deviation, variance)
from a file containing numbers.
"""

import sys
import time

def compute_mean(numbers):
    """Compute the mean of a list of numbers."""
    total = sum(numbers)
    count = len(numbers)
    return total / count

def compute_median(numbers):
    """Compute the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    count = len(sorted_numbers)
    middle = count // 2
    if count % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    return sorted_numbers[middle]

def compute_mode(numbers):
    """Compute the mode of a list of numbers."""
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_frequency = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_frequency]
    return modes[0] if len(modes) == 1 else modes

def compute_variance(numbers, mean_value):
    """Compute the variance of a list of numbers."""
    squared_diffs = [(num - mean_value) ** 2 for num in numbers]
    return sum(squared_diffs) / len(numbers)

def compute_standard_deviation(variance_value):
    """Compute the standard deviation given variance."""
    return variance_value ** 0.5

def process_file(file_path):
    """Process the input file and compute statistics."""
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                try:
                    number = float(line)
                    numbers.append(number)
                except ValueError:
                    print(f"Invalid data: {line}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    if not numbers:
        print("No valid numbers found in the file.")
        sys.exit(1)
    mean_value = compute_mean(numbers)
    median_value = compute_median(numbers)
    mode_value = compute_mode(numbers)
    variance_value = compute_variance(numbers, mean_value)
    std_dev_value = compute_standard_deviation(variance_value)
    return mean_value, median_value, mode_value, variance_value, std_dev_value

def main():
    """Main function to execute the statistics computation program."""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)
    file_path = sys.argv[1]
    start_time = time.time()
    mean_value, median_value, mode_value, variance_value, std_dev_value = process_file(file_path)
    elapsed_time = time.time() - start_time
    results = [
        f"Mean: {mean_value}",
        f"Median: {median_value}",
        f"Mode: {mode_value}",
        f"Variance: {variance_value}",
        f"Standard Deviation: {std_dev_value}",
        f"Execution time: {elapsed_time:.6f} seconds"
    ]
    for line in results:
        print(line)
    with open("StatisticsResults.txt", "w", encoding='utf-8') as result_file:
        result_file.write("\n".join(results))

if __name__ == "__main__":
    main()
