class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0],-x[1]))
        print(intervals)
        
        END = 1
        START = 0
        
        count = 0

        prev = intervals[0]
        for curr in intervals[1:]:

            if prev[END] > curr[START]:
                count+=1
                prev = [curr[START],min(prev[END],curr[END])]
            else:
                prev = curr
        return count