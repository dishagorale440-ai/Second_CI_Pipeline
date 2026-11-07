def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    matrix = []

    for i in range(rows):
        row = list(map(int, input("Enter row values separated by spaces: ").split()))
        matrix.append(row)

    print(transpose_matrix(matrix))
