# class Solution:
#     # TC -> N, SC -> 1
#     def search(self, nums: List[int], target: int) -> int:
#         if target not in nums:
#             return -1
#         return nums.index(target)

class Solution:
    # TC -> N, SC -> 1
    def bs(self, left, right, nums, target):
        if left > right:
            return -1
        mid = left + (right - left)//2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.bs(mid+1, right, nums, target)
        return self.bs(0, mid - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.bs(0, len(nums) - 1, nums, target)

        