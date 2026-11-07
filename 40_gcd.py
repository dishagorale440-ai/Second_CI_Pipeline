def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return abs(a)


if __name__ == "__main__":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(find_gcd(a, b))
