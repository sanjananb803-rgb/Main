def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def is_palindrome(n):
    if n < 0:
        return False
    return str(n) == str(n)[::-1]
def is_even(n):
    return n % 2 == 0
def main():
    print("===== NUMBER UTILITIES TOOLKIT =====")
    num = int(input("Enter a number: "))
    print("Prime Number:", is_prime(num))
    print("Factorial:", factorial(num))
    print("Palindrome:", is_palindrome(num))
    print("Even Number:", is_even(num))
if __name__ == "__main__":
    main()
