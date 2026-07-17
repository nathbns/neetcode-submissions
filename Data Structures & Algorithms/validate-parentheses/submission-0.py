class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                print("c = ", c)
                print("closeToOpen[", c, "] = ", closeToOpen[c])
                if stack and stack[-1] == closeToOpen[c]:
                    print(
                        "(stack[-1]) = ", stack[-1], " == ", "(closeToOpen[ ", c, " ]) = ",closeToOpen[c]
                    )
                    stack.pop()
                    print("pop: stack = ", stack)
                else:
                    return False
            else:
                stack.append(c)
                print("append to stack = ", c)
                print("stack = ", stack)
        
        return True if not stack else False