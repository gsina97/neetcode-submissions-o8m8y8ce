class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        cars = []

        for i in range(len(speed)):
            cars.append([position[i], speed[i]])
        
        cars.sort(reverse = True)

        fleet = 0
        slowest_arrival = 0

        for pos, spd in cars:

            t = (target - pos)/spd

            if t > slowest_arrival:
                slowest_arrival = t
                fleet += 1
        
        return fleet