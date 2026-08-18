class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        
        cars.sort(reverse=True)

        slowest_to_target = 0
        fleets = 0

        for position,speed in cars:
            target_time = (target - position) / speed

            if target_time > slowest_to_target:
                fleets += 1
                slowest_to_target = target_time
        
        return fleets
