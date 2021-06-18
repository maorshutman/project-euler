
def main():
    e_rep = [1, 2]
    for k in range(2, 35):
        e_rep += [1, 1, 2 * k]

    start_idx = 98

    numer = e_rep[start_idx]
    denom = 1

    for i in range(start_idx-1, -1, -1):
        tmp_num = numer
        numer = numer * e_rep[i] + denom
        denom = tmp_num

    # Final 1 / (num/denom).
    denom, numer = numer, denom
    final_numer = 2 * denom + numer
    print(final_numer)

    # Sum digits.
    sum_of_digits = 0
    while final_numer != 0:
        sum_of_digits += (final_numer % 10)
        final_numer = final_numer // 10

    print(f"Sum of digits = {sum_of_digits}")


if __name__ == "__main__":
    main()
