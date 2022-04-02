from itertools import combinations
import itertools
import math


def plus(a, b):
    return a+b


def minus(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    if b != 0.:
        return a/b
    else:
        return float("nan")


_STR_TO_OP = {
    "+": plus,
    "-": minus,
    "*": mul,
    "/": div,
}


def compute(abcd, op_seqs):
    ints = set()

    for x0, x1, x2, x3 in itertools.permutations(abcd):
        for ops in op_seqs:

            op1 = _STR_TO_OP[ops[0]]
            op2 = _STR_TO_OP[ops[1]]
            op3 = _STR_TO_OP[ops[2]]

            r1 = op3(op2(op1(x0, x1), x2), x3)
            r2 = op3(x3, op2(op1(x0, x1), x2))
            r3 = op3(op2(x2, op1(x0, x1)), x3)
            r4 = op3(x3, op2(x2, op1(x0, x1)))

            for res in [r1, r2, r3, r4]:
                if (not math.isnan(res)) and (res > 0.) and (res == round(res)):
                    ints.add(int(res))

    return ints


def seq_len(poss_ints: set):
    poss_ints = sorted(list(poss_ints))
    n = 0
    for i, pi in enumerate(poss_ints):
        if not (i+1 == pi):
            break
        n += 1
    return n


def main():

    ops = ["+", "*", "-", "/"]
    ops_combs = []
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                ops_combs.append([op1, op2, op3])

    digits = [float(i) for i in range(1, 10)]
    combs = list(combinations(digits, 4))

    best = None
    max_seq = 0
    for comb in combs:
        poss_ints = compute(comb, ops_combs)

        l = seq_len(poss_ints)
        if max_seq < l:
            best = comb
            max_seq = l

    print(max_seq, best)


if __name__ == "__main__":
    main()
