class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                print("int:", int(token))
                return int(token)
            right = dfs()
            left = dfs()

            if token == '+':
                print('+: ', left, " + ", right, " = ", left + right)
                return left + right
            elif token == '-':
                print('-: ', left, " - ", right, " = ", left - right)
                return left - right
            elif token == '*':
                print('*: ', left, " * ", right, " = ", left * right)
                return left * right
            elif token == '/':
                print('/: ', left, " / ", right, " = ", int(left / right))
                return int(left / right)
        
        return dfs()
