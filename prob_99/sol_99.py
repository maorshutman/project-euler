import numpy as np


def main():

    with open('p099_base_exp.txt') as f:
        base_exp = []
        for line in f:
            tokens = line.rstrip().split(',')
            base_exp.append([int(tokens[0]), int(tokens[1])])

    logs = []
    for base, exp in base_exp:
        logs.append(np.log(base) * exp)

    print(np.argmax(logs))


if __name__ == "__main__":
    main()
