class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_ptr = 0
        nums2_ptr = 0
        while (nums2_ptr < n):
            if (nums2[nums2_ptr] < nums1[nums1_ptr]):
                # Shift elements in nums1 right
                for i in range(m + nums2_ptr, nums1_ptr, -1):
                    nums1[i] = nums1[i - 1]

                nums1[nums1_ptr] = nums2[nums2_ptr]
                nums2_ptr += 1
            elif (nums1_ptr >= m + nums2_ptr):
                nums1[nums1_ptr] = nums2[nums2_ptr]
                nums2_ptr += 1

            nums1_ptr += 1