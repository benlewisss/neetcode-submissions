class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()

        insert_pointer = 0

        for scan_pointer in range(len(nums)):
            if nums[scan_pointer] not in seen:
                nums[insert_pointer] = nums[scan_pointer]
                seen.add(nums[scan_pointer]) 
                insert_pointer += 1
                
        return insert_pointer
            

