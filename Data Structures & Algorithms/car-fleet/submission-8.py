class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        # monotonically decreasing
        # for each car in reverse, if it arrivese equal or after of that time, its part of the same fleet. else push to stack

        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for p,s in cars:

            time = (target - p) / s

            if stack and time > stack[-1]:
                stack.append(time)
            
            if not stack:
                stack.append(time)
        return len(stack)
