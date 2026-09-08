from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = []
        res_dict = defaultdict()

        for word in strs:
            sort = str(sorted(word))
            if sort in res_dict:
                res_dict[sort].append(word)
            else:
                res_dict[sort] = [word]
                keys.append(sort)

        res = []
        for key in keys:
            res.append(res_dict[key])
        return res
        
            
        