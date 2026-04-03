class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # map position of a car to its speed
        cars = list(zip(position, speed))

        # sort by position, Largest -> smallest
        cars.sort(reverse=True)
        stack = []

        for position, speed in cars:
            # calculate when that car arrives at the end
            time = (target - position) / speed

            # if no cars in stack, it forms the first fleet
            if not stack:
                stack.append(time)
            else:
                # if it arrives after the car it meets ahead, 
                #  then it will have to form a new fleet.
                if time > stack[-1]:
                    stack.append(time)
        
        return len(stack)