class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        len_nums = len(nums)

        if len_nums == 1:
            return nums[0]

        L = 0
        R = len_nums - 1

        while L <= R:
            middle = L + ((R - L) // 2)

            if L == R:
                break
            if nums[middle] < nums[middle - 1]:
                break

            if nums[middle] > nums[R]:
                L = middle + 1
            else:
                R = middle - 1
            
        return nums[middle]