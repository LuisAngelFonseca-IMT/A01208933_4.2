"""
Module for counting distinct words and their frequencies from a file.
"""

import sys
import time

def count_words(file_path):
    """Process the input file, count distinct words and their frequencies, and handle errors."""
    word_counts = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    cleaned_word = ''.join(c for c in word if c.isalnum()).lower()
                    if cleaned_word:
                        if cleaned_word in word_counts:
                            word_counts[cleaned_word] += 1
                        else:
                            word_counts[cleaned_word] = 1
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    return word_counts

def main():
    """Main function to execute the word count program."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)
    file_path = sys.argv[1]
    start_time = time.time()
    word_counts = count_words(file_path)
    elapsed_time = time.time() - start_time
    results = [f"{word}: {count}" for word, count in sorted(word_counts.items())]
    results.append(f"Execution time: {elapsed_time:.6f} seconds")
    for line in results:
        print(line)
    with open("WordCountResults.txt", "w", encoding='utf-8') as result_file:
        result_file.write("\n".join(results))

if __name__ == "__main__":
    main()
