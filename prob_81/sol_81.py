import csv


def get_min(i, j, matrix, min_dist):
    n = len(matrix)

    down = None
    right = None

    if i+1 < n:
        down = min_dist[i + 1][j]
    if j+1 < n:
        right = min_dist[i][j + 1]

    diff = 0
    if down is not None and right is not None:
        diff = min(right, down)
    elif down is None and right is not None:
        diff = right
    elif right is None and down is not None:
        diff = down

    return diff + matrix[i][j]


def main():

    with open("prob_81/p081_matrix.txt", newline='') as f:
        reader = csv.reader(f)
        matrix = []
        for row in reader:
            matrix.append([int(i) for i in row])

    n = len(matrix)
    min_dist = [[0] * n for _ in range(n)]

    for i in range(n-1, -1, -1):
        for r in range(n-1, i, -1):
            min_dist[r][i] = get_min(r, i, matrix, min_dist)

        for c in range(n-1, i-1, -1):
            min_dist[i][c] = get_min(i, c, matrix, min_dist)

    print(min_dist[0][0])


if __name__ == "__main__":
    main()
