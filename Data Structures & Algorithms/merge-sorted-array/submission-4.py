class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Point to the end of the valid data in each array
        nums1_ptr = m - 1      # last valid element in nums1
        nums2_ptr = n - 1      # last element in nums2
        insert_ptr = m + n - 1 # last position in nums1 (the back)
        
        while nums2_ptr >= 0:
            if nums1_ptr >= 0 and nums1[nums1_ptr] > nums2[nums2_ptr]:
                nums1[insert_ptr] = nums1[nums1_ptr]
                nums1_ptr -= 1
            else:
                nums1[insert_ptr] = nums2[nums2_ptr]
                nums2_ptr -= 1
            insert_ptr -= 1