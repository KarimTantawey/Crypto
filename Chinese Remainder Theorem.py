
import sys

# Force UTF‐8 encoding of stdout (Python 3.7+)
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

def inv_mod(a: int, m: int) -> int:
    """Return the modular inverse of a modulo m."""
    return pow(a, -1, m)

def crt(a_list: list[int], n_list: list[int]) -> tuple[int, int]:
    """
    Given remainders a_list and pairwise‐coprime moduli n_list,
    returns (x, N) where x is the unique solution modulo N = prod(n_list).
    """
    # Compute the product of all moduli
    N = 1
    for n in n_list:
        N *= n

    x = 0
    for a_i, n_i in zip(a_list, n_list):
        N_i = N // n_i
        M_i = inv_mod(N_i, n_i)
        x += a_i * N_i * M_i

    return x % N, N

def main():
    # Define the congruences
    a_list = [2, 3, 5]
    n_list = [5, 11, 17]

    # Solve via CRT
    x, N = crt(a_list, n_list)

    # Display the result using only ASCII
    print(f"Solution: x == {x} (mod {N})")
    for a_i, n_i in zip(a_list, n_list):
        print(f"x % {n_i} = {x % n_i}  (should be {a_i})")

if __name__ == "__main__":
    main()
