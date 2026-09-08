from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = set()
        freq_map = defaultdict(list)

        for string in strs:
            freq_arr = [0] * 26
            freq = Counter(string)
            for c in freq:
                freq_arr[ord(c) - 97] = freq[c]
            keys.add(str(freq_arr))
            freq_map[str(freq_arr)].append(string)
        
        res = []
        for key in keys:
            res.append(freq_map[key])
        return res