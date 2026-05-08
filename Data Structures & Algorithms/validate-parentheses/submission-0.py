class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        lookUp = {']':'[', '}':'{',')':'('}

        for i in range(len(s)):
            if s[i] in lookUp:
                if stack and lookUp[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
            print(stack)
        return True if not stack else False
        