from collections import defaultdict

class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = defaultdict()

        def rob_from_house(house_num: int, robbed_first: bool = False) -> int:
            if house_num >= len(nums):
                return 0
            
            if house_num == len(nums) - 1 and robbed_first == True:
                return 0

            if (house_num, robbed_first) not in cache:
                cache[(house_num, robbed_first)] = max(nums[house_num] + rob_from_house(house_num + 2, (True if house_num == 0 else False) or robbed_first), rob_from_house(house_num + 1, robbed_first))

            return cache[(house_num, robbed_first)]

        return rob_from_house(0)
