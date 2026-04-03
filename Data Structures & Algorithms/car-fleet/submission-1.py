class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # map position of a car to its speed
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []
        for position, speed in cars:
            time = (target - position) / speed

            if not stack:
                stack.append(time)
            else:

                if time > stack[-1]:
                    stack.append(time)
        
        return len(stack)