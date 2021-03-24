from typing import List


def runningSum(nums: List[int]) -> List[int]:
    ret_sum = []
    k = 0
    for i in range(0, len(nums)):
        if i == 0:
            k = nums[i]
            ret_sum.append(k)
        else:
            k = k + nums[i]
            ret_sum.append(k)
    return ret_sum


if __name__ == '__main__':
    print(runningSum([1, 2, 3, 4]))
