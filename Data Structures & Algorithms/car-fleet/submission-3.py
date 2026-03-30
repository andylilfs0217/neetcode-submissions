class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        speed_map = {}
        for i, pos in enumerate(position):
            s = speed[i]
            speed_map[pos] = s
        
        sorted_position = sorted(position)
        ans = 0
        leading_fleet_time = 0
        i = n-1
        while i >= 0:
            pos = sorted_position[i]
            s = speed_map[pos]
            t = (target - pos) / s
            print(pos, s, t, leading_fleet_time)
            if t > leading_fleet_time:
                ans += 1
                leading_fleet_time = t
            print(ans)
            i -= 1

            
        return ans