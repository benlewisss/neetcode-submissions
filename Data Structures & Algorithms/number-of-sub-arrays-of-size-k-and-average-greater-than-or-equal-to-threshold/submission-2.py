class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        numSubarrays = 0
        rollingSum = sum(arr[:k])

        rollingAverage = rollingSum / k
        if (rollingAverage >= threshold):
                numSubarrays += 1

        for R in range(k, len(arr)):
            rollingSum -= arr[R - k]
            rollingSum += arr[R]

            rollingAverage = rollingSum / k
            if (rollingAverage >= threshold):
                numSubarrays += 1
            
            

        return numSubarrays    
            

