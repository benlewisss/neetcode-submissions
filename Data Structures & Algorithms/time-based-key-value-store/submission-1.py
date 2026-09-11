# Solved in 20 minutes without help (But tbf I did the other two binary search ones right before this)
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list[tuple])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        timemap = self.hashmap[key]
        len_timemap = len(timemap)
        
        L = 0
        R = len_timemap - 1
        while L <= R:

            middle = L + ((R - L) // 2)

            if timemap[middle][0] <= timestamp and (middle + 1 >= len_timemap or timemap[middle + 1][0] > timestamp):
                return timemap[middle][1]

            if timestamp > timemap[middle][0]:
                L = middle + 1
            else:
                R = middle - 1

        return ""

            
            

        
