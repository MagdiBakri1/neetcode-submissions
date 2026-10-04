class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ins = n *[0];
        stack = []
        for i in range(0, n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                k=stack.pop()
                ins[k] = i - k
            stack.append(i)
        return ins     