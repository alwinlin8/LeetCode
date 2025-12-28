import heapq

class Solution(object):
    def mostBooked(self, n, meetings):
        meetings.sort()

        avail_room = list(range(n))
        heapq.heapify(avail_room)

        occup_room = []  # (end_time, room)
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free all rooms that are done before this meeting starts
            while occup_room and occup_room[0][0] <= start:
                end_time, room = heapq.heappop(occup_room)
                heapq.heappush(avail_room, room)

            if avail_room:
                room = heapq.heappop(avail_room)
                finish = start + duration
            else:
                end_time, room = heapq.heappop(occup_room)
                finish = end_time + duration

            heapq.heappush(occup_room, (finish, room))
            count[room] += 1

        return count.index(max(count))
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        