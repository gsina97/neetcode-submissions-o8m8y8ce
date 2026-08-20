class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = 0
        min_time = 0

        cars = []

        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars.sort(reverse=True)

        for pos, spd in cars:
            
            t = (target - pos)/spd

            if t > min_time:
                fleets += 1
                min_time = t
        
        return fleets

        
