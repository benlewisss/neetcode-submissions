class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_nums = list()

        rolling_sum = 0
        for num in nums:
            rolling_sum += num
            self.prefix_nums.append(rolling_sum)

    def sumRange(self, left: int, right: int) -> int:
        return ((self.prefix_nums[right] - self.prefix_nums[left - 1]) if left >= 1 else (self.prefix_nums[right] - 0))


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)