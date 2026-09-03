class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        len_nums = len(nums)
        prefix_sum = [1] * len_nums
        postfix_sum = [1] * len_nums
        res = [1] * len_nums

        for i in range(0, len_nums):
            prefix_sum[i] = (nums[i] * prefix_sum[i - 1]) if i >= 1 else nums[i]
            postfix_sum[-i - 1] = (nums[-i - 1] * postfix_sum[-i]) if i >= 1 else nums[-i - 1]

        for i in range(0, len_nums):
            res[i] = (prefix_sum[i - 1] if i >= 1 else 1) * (postfix_sum[i + 1] if (i+1) < len_nums else 1)

        return res