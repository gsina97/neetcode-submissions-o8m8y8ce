class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        cars = []

        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        
        cars.sort(reverse=True)
        slowest_t = 0
        groups = 0

        for pos, spd in cars:

            t = (target - pos) / spd
            if t > slowest_t:
                slowest_t = t
                groups += 1


        return groups 

