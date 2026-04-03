class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # numbers of car
        stack = []

        cars = list(zip(position, speed))

        cars.sort(reverse=True)

        for pos, spd in cars:
            time = (target - pos) / spd

            if stack and time > stack[-1]:
                stack.append(time)
            
            if not stack:
                stack.append(time)
        
        return len(stack)
            