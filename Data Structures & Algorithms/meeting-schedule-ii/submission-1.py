"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #input: an array of interval times -> [start, end]
        #output: the minimum number of rooms need to schedule all meetings

        #1 room is required if there are no conflicts in meeting times
        #if a conflict occurs another room is required

        # 0 - 40, 5 - 10, 15 - 20  
        #    1, 2, 2

        #pattern we are re-checking if conflixt arrising from already scheduled meeting
        #if conflict, then we get # of room to the conflict + 1 else no conflict use that amount of rooms
        #DP problem

        #room[i] = the minimum amount of rooms needed to schdule meeting up to intervals i + [ending times for those rooms]
        #base case: room[0] = [1, [nums[0].end_time] ] as any meeting requires at least one room
        #solution: room[n][0] 
        #formula: room[i] = room[i-1], check if end_times have any conflict if so increment by 1
        start = intervals.copy()
        end = intervals.copy()
        start.sort(key=lambda x: x.start)
        end.sort(key=lambda x: x.end)

        res = count = 0
        s = e = 0

        while s < len(intervals):
            if start[s].start < end[e].end:
                count+=1
                s+=1
            else:
                e+=1
                count-=1
            res = max(res, count)
        return res







