def subtractProductAndSum(n: int) -> int:
    n_array = [int(d) for d in str(n)]
    sum_of_n = sum(n_array)
    mul_of_n = 1
    for i in n_array:
        mul_of_n *= i
    return abs(mul_of_n - sum_of_n)


if __name__ == "__main__":
    print(subtractProductAndSum(12))
