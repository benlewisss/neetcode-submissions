class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = Counter(s)
        counter2 = Counter(t)

        if counter1 == counter2:
            return True
        return False