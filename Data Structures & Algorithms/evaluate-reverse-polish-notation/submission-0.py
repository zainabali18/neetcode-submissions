import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {"+": operator.add, "-": operator.sub,
                  "*": operator.mul, "/": operator.truediv}
        stack = []
        for token in tokens:
            if token in operations:
                right = stack.pop()
                left = stack.pop()
                stack.append(int(operations[token](left, right)))
            else:
                stack.append(int(token))
        return stack.pop()