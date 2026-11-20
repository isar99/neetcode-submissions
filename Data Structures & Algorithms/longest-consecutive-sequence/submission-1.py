class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        len_nums = len(nums)
        if len_nums < 1:
            return 0
        x = []
        i = 0
        while i < len_nums:
            r = [nums[i]]
            j = i + 1

            while j < len_nums and (nums[j] == nums[j-1]+1):
                r.append(nums[j])
                j += 1
            x.append(r)
            i = j
        x_len = []
        for num in x:
            x_len.append(len(num))
        return max(x_len)
