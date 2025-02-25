def is_power_of_two(n):
    """Bir sayının 2'nin kuvveti olup olmadığını kontrol eder."""
    return (n & (n - 1)) == 0

def collatz(n):
    """Collatz dizisini oluşturur."""
    sequence = [n]
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    return sequence

def run_collatz_up_to(max_n):
    """Bitiş değerine kadar olan 2'nin kuvveti olmayan çift sayılar için Collatz uygular."""
    for n in range(2, max_n + 1, 2):  # Sadece çift sayılar
        if not is_power_of_two(n):    # 2'nin kuvveti olmayanları seç
            sequence = collatz(n)
            print(f"Collatz({n}): {sequence}")

# Örnek Kullanım
run_collatz_up_to(20)
