from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)

        for string in strs:

            # Could further optimise this by doing the freq count in one pass without using counter, and just incrementing the values directly in freq arr
            freq_arr = [0] * 26
            freq = Counter(string)
            for c in freq:
                # ord returns ascii char code, so -97 to get back into range
                freq_arr[ord(c) - 97] = freq[c]

            # Using tuple because keys need to be immutable (could also use string)
            freq_map[tuple(freq_arr)].append(string)
        
        return list(freq_map.values())