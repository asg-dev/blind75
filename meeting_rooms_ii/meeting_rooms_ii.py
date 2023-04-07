class Solution:
    # Two Pointers (Chronological Ordering)
    def minimumMeetingRooms(self, intervals):

      # edge cases
      if not intervals or not intervals[0]:
        return 0

      starts = [start for start, end in intervals]
      ends = [end for start, end in intervals]

      starts.sort()
      ends.sort()

      i = 1
      j = 0
      gmax = 0
      rooms_required = 1

      while i < len(starts):
        if starts[i] < ends[j]:
          rooms_required += 1
          i += 1
        else:
          rooms_required -= 1
          j += 1
        gmax = max(gmax, rooms_required)

      return rooms_required



sol = Solution()
print(sol.minimumMeetingRooms([[7, 30], [1, 6], [9, 10], [5, 15]]))
print(sol.minimumMeetingRooms([[0, 30], [5, 10], [10, 20], [25, 35]]))
print(sol.minimumMeetingRooms([[]]))
print(sol.minimumMeetingRooms([]))
