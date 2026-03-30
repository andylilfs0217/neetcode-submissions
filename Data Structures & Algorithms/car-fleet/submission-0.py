class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def cal_time(pos: int, s: int) -> float:
            return (target-pos)/s

        speed_map = defaultdict(int)
        for i, pos in enumerate(position):
            s = speed[i]
            speed_map[pos] = s
        
        sorted_pos = sorted(position)
        res = 0

        sorted_times = [cal_time(pos, speed_map[pos]) for pos in sorted_pos]
        last_time = 0
        while len(sorted_times) > 0:
            curr_time = sorted_times.pop()
            if last_time < curr_time:
                res += 1
                last_time = curr_time
        return res
