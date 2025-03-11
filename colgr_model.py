import matplotlib.pyplot as plt

def is_power_of_two(n):
    """Checks whether a number is a power of 2."""
    return (n & (n - 1)) == 0

def collatz_steps(n):
    """Calculates how many steps are required to bring a number to 1."""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def visualize_collatz_steps(max_n):
    """Visualizes Collatz step counts for even numbers that are not powers of 2."""
    numbers = []
    steps = []

    for n in range(2, max_n + 1, 2):  # Only even numbers
        if not is_power_of_two(n):    # Choose those that are not powers of 2
            numbers.append(n)
            steps.append(collatz_steps(n))

    plt.figure(figsize=(10, 5))
    plt.scatter(numbers, steps, color='blue', alpha=0.7)
    plt.xlabel("Initial Number")
    plt.ylabel("Number of Transactions to Reach 1")
    plt.title("Collatz Operation Numbers for Even Numbers That Are Not Powers of 2")
    plt.grid(True)
    plt.show()

# Example Usage
visualize_collatz_steps(100)
