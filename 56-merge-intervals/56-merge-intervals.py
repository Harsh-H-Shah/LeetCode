def f(x):
    return x[0]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = f)
        res = []
        curr=intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if curr[1]<interval[0]:
                res.append(curr)
                curr = interval
            else:
                curr[1] = max(curr[1], interval[1])
        res.append(curr)
        return res