class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars.sort(reverse=True)


        fleets = 0
        slowest_arrival = 0

        for pos, spd in cars:

            arrival = (target - pos) / spd

            if arrival > slowest_arrival:
                fleets += 1
                slowest_arrival = arrival
        
        return fleets

