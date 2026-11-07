def find_missing_number(numbers, n):
    missing = 0

    for number in range(1, n + 1):
        missing ^= number

    for number in numbers:
        missing ^= number

    return missing


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    n = int(input("Enter the total number of values: "))
    print(find_missing_number(numbers, n))
