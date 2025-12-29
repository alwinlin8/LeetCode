class Solution(object):
    def exclusiveTime(self, n, logs):
        sol = [0] * n
        stack = []
        previous_start_time = 0

        for i in logs:
            func_id, call_type, timestamp = i.split(':')
            func_id = int(func_id)
            timestamp = int(timestamp)

            if call_type == "start":
                if stack:
                    sol[stack[-1]] += timestamp - previous_start_time 
                stack.append(func_id)
                previous_start_time = timestamp
            else:
                sol[stack.pop()] += timestamp - previous_start_time + 1
                previous_start_time = timestamp + 1
        return sol


        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        