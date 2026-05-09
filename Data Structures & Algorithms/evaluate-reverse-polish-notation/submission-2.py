class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i,ch in enumerate(tokens):
            if ch=="+":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a+b)
            elif ch=="-":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a-b)
            elif ch=="*":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a*b)
            elif ch=="/":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(int(float(a)/b))
            else:
                stack.append(int(ch))
        return stack[0]

        