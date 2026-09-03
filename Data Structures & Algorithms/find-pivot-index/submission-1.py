class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = list()
        rolling_sum = 0
        for num in nums:
            rolling_sum += num
            prefix_sum.append(rolling_sum)

        len_nums = len(nums)
        for i in range(len_nums):
            sum_left = (prefix_sum[i - 1] if i >= 1 else 0)
            sum_right = prefix_sum[len_nums - 1] - prefix_sum[i]
            if (sum_left == sum_right):
                return i

        return -1
