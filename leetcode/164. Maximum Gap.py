from typing import List


def maximumGap(nums: List[int]) -> int:
    if len(nums) >= 2:
        nums.sort()
        return max([nums[i+1]-nums[i] for i in range(len(nums)-1)])
    return 0


print(maximumGap([3]))
