from typing import List


class BS:
    def __init__(self,  nums: List[int]):
        nums.sort()
        self.nums = nums

    def binary_search(self, target: int) ->int:

        return self.recursive_binary_search(self.nums, target, 0, len(self.nums) - 1)

    def recursive_binary_search(self, nums: List[int], target:int, left:int, right: int) -> int:

        if left > right:
            return -1

        mid = (left + right) // 2

        if target < nums[mid]:
            return self.recursive_binary_search(nums, target, left, mid - 1)
        if target > nums[mid]:
            return self.recursive_binary_search(nums, target, mid + 1, right)

        return mid


bs = BS([0,-1,3,9,5,12])
print(bs.binary_search(9))

bs = BS([0,-1,3,9,5,12])
print(bs.binary_search(2))
