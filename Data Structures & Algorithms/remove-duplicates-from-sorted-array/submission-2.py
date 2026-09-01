class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_pointer = 1

        for scan_pointer in range(1, len(nums)):
            if nums[scan_pointer] != nums[insert_pointer - 1]:
                nums[insert_pointer] = nums[scan_pointer]
                insert_pointer += 1

        return insert_pointer
            

