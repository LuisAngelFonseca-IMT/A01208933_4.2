"""
Module for converting numbers from a file to binary and hexadecimal representations.
"""

import sys
import time

def int_to_binary(number):
    """Convert an integer to its binary representation using a basic algorithm."""
    if number == 0:
        return "0"
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

def int_to_hexadecimal(number):
    """Convert an integer to its hexadecimal representation using a basic algorithm."""
    hex_digits = "0123456789ABCDEF"
    if number == 0:
        return "0"
    hexadecimal = ""
    while number > 0:
        remainder = number % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        number //= 16
    return hexadecimal

def process_file(file_path):
    """Process the input file, convert numbers, and handle errors."""
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                number_str = line.strip()
                try:
                    number = int(number_str)
                    binary = int_to_binary(number)
                    hexadecimal = int_to_hexadecimal(number)
                    results.append(f"{number}: Binary={binary}, Hexadecimal={hexadecimal}")
                except ValueError:
                    error_msg = f"Invalid data: {number_str}"
                    print(error_msg)
                    results.append(error_msg)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    return results

def main():
    """Main function to execute the conversion program."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)
    file_path = sys.argv[1]
    start_time = time.time()
    results = process_file(file_path)
    elapsed_time = time.time() - start_time
    results.append(f"Execution time: {elapsed_time:.6f} seconds")
    for line in results:
        print(line)
    with open("ConvertionResults.txt", "w", encoding='utf-8') as result_file:
        result_file.write("\n".join(results))

if __name__ == "__main__":
    main()
