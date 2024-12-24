def print_alphabet_pattern_map_join(n):
    for i in range(n):
        # Print leading spaces
        print(" " * (n - i - 1), end="")

        # Use map() to generate the increasing sequence and decreasing sequence
        increasing_part = list(map(lambda x: chr(65 + x), range(i + 1)))
        decreasing_part = list(map(lambda x: chr(65 + x), range(i - 1, -1, -1)))

        # Join and print the parts of the row
        print(" ".join(increasing_part + decreasing_part))

# Example usage:
n = 3
print_alphabet_pattern_map_join(n)
