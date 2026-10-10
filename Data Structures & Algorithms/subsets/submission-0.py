class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(index, current_path):
            if index >= len(nums):
                output.append(current_path.copy())
                return

            current_path.append(nums[index])
            dfs(index + 1, current_path)

            current_path.pop()
            dfs(index + 1, current_path)

        dfs(0, [])
        return output