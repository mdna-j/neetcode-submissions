class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
         # Pair up positions and speeds, and sort them in reverse order (closest to target first)
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        max_time = 0
        
        for pos, spe in cars:
            # Calculate time to reach target for the current car
            time_to_target = (target - pos) / spe
            
            # If this car takes longer than the slowest car ahead of it, it forms a new fleet
            if time_to_target > max_time:
                fleets += 1
                max_time = time_to_target
                
        return fleets