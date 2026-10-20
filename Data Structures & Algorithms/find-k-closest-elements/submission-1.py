class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L = 0
        R = 0
        
        num_found = 0
        while R < len(arr):
            
            # Window contains > K values, we must choose choose how to shrink
            if (R - L + 1) > k:
                # if arr[R] is closer to x than arr[L] OR arr[R] and arr[L] are the same (we want to keep exploring), we shrink from left
                if abs(arr[R] - x) < abs(arr[L] - x) or (arr[L] == arr[R]):
                    L += 1
                    continue
                # if arr[L] is closer to x than arr[R], we have found the closest values, return early
                else:
                    break
            R += 1


        return arr[L:R]