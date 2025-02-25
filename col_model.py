def is_power_of_two(n):
    """Checks whether a number is a power of 2."""
    return (n & (n - 1)) == 0

def collatz(n):
    """Creates the Collatz array."""
    sequence = [n]
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    return sequence

def run_collatz_up_to(max_n):
    """Applies Collatz for even numbers that are not powers of 2 up to the end value."""
    for n in range(2, max_n + 1, 2):  # Only even numbers
        if not is_power_of_two(n):    # Choose those that are not powers of 2
            sequence = collatz(n)
            print(f"Collatz({n}): {sequence}")

# Example Usage
run_collatz_up_to(20)
