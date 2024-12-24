def print_triangle_while(n):
    i = 1
    while i <= n:
        # Print leading spaces to align the triangle
        print(" " * (n - i), end="")
        # Print numbers for each row
        j = 1
        while j < 2 * i:
            print(j, end=" ")
            j += 1
        print()  # Move to the next line
        i += 1

# usage:
print_triangle_while(3)