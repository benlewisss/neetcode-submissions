class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_nums = len(nums)

        
        for i in range(0, len_nums-1):
            if nums[i] != val:
                continue
            
            right_ptr = 1
            while (nums[i+right_ptr] == val):
                right_ptr += 1
                if (i+right_ptr >= len_nums):
                    break
                    
            if (i+right_ptr >= len_nums):
                    break        

            print(nums)
            nums[i], nums[i+right_ptr] = nums[i+right_ptr], nums[i]
            print(nums)

        k = 0
        for num in nums:
            if num != val: k += 1
            
        return k
