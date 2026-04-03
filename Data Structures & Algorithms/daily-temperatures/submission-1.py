class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = len(temperatures) * [0]
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idxPopped = stack.pop()
                output[idxPopped] = idx - idxPopped
            stack.append(idx) 
        
        return output
            
            
        
        