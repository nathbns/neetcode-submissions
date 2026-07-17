class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                print(
                    "stackT = ", stackT,
                    ", stackInd = ", stackInd
                )
                res[stackInd] = i - stackInd
                print(
                    "res[", stackInd, "] = ",
                    res[stackInd]
                )
            stack.append((t, i))
            print("stack = ", stack)
        
        return res