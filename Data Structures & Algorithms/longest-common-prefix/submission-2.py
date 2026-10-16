class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest_prefix = list()
        largest_possible_prefix = len(min(strs, key=len))

        ptr = 0
        while ptr < largest_possible_prefix:
            curr_val = strs[0][ptr]
            for string in strs:
                if string[ptr] != curr_val:
                    return "".join(longest_prefix)
            longest_prefix.append(curr_val)
            ptr += 1

        return "".join(longest_prefix)