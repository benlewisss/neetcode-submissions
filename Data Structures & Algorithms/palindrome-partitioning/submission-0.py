# Watched up to minute 5 of the neetcode video on this - once I saw how he drew the decision tree it made much more sense, 
# so I decided to program from there.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # def backtracking(path, choices):
        #     if is_base_case(path):
        #         all_palindromes.append(path.copy())

        #     for choice in choices:
        #         if is_valid_choice(choice):

        #             path.append(choice)
        #             backtracking(path, updated_choices)

        #             path.pop()
        #             backtracking(path, choices)

        def is_valid_palindrome(string_array: list) -> bool:

            len_string_array = len(string_array)

            if len_string_array == 0:
                return False

            if len_string_array == 1:
                return True

            left = 0
            right = len_string_array - 1

            while left < right:
                if string_array[left] != string_array[right]:
                    return False
                left += 1
                right -= 1

            return True

        
        all_partitions = []
        curr_partition = []

        def backtracking(index):
            if index >= len(s):
                all_partitions.append(curr_partition.copy())
                return

            # Are choices at each level essentially consist of where do we want to splice
            # the input string on this iteration
            for i in range(index + 1, len(s) + 1):
                partition = s[index:i]
                if is_valid_palindrome(partition):
                    curr_partition.append("".join(partition))
                    backtracking(i)

                    curr_partition.pop()

        backtracking(0)
        return all_partitions


