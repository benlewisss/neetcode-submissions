class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # HINT USED:
        # Your recursive function takes two parameters: pointer and max_encountered. When you reach index pointer, whether you can take nums[pointer] depends on max_encountered. Therefore, memoizing on pointer alone causes incorrect cached values to be reused with different prior values.


        memo = {}
        def backtracking(pointer, max_encountered):
            if pointer >= len(nums):
                return 0

            if ((pointer, max_encountered) not in memo):
                sequence_length1 = sequence_length2 = 0
                if nums[pointer] > max_encountered:
                    sequence_length1 = 1 + backtracking(pointer + 1, nums[pointer])

                sequence_length2 += backtracking(pointer + 1, max_encountered)
                memo[(pointer, max_encountered)] = max(sequence_length1, sequence_length2)

            return memo[(pointer, max_encountered)]
            
        return backtracking(0, -9999)