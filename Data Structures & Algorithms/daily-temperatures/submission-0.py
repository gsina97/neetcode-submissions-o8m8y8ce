class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        output = [0] * len(temperatures)
        

        for idx,val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                    i = stack.pop()
                    output[i] = idx - i
            stack.append(idx)
        
        return output


        