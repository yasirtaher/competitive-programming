from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    res = []
    x = nums[:n]
    y = nums[n:]
    for i in range(0, n):
        res.append(x[i])
        res.append(y[i])
    return res


if __name__ == '__main__':
    print(shuffle([2, 5, 1, 3, 4, 7], 3))
