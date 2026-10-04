class Solution:
    stack = []
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.lstrip("-").isdigit():
                 stack.append(int(i))
            else:
                first =stack[-1]
                stack.pop()
                second = stack[-1]
                stack.pop()
                if i =="+":
                    calc = second+first
                elif i =="-":
                    calc = second-first
                elif i =="*":
                    calc = second * first
                else :
                    calc = int(second / first)
                stack.append(calc)
        return int(stack[-1])