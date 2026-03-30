class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for elem in tokens:
            if elem == '+':
                stack.append(stack.pop()+stack.pop())
            elif elem == '-':
                b=stack.pop()
                a=stack.pop()
                stack.append(a-b)
            elif elem == '*':
                stack.append(stack.pop()*stack.pop())
            elif elem == '/':
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(elem))
        return stack[0]
            