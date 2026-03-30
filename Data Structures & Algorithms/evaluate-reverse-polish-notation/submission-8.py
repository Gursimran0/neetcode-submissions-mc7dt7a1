class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        array = []
        for elem in tokens:
            if elem == "+":
                x=int(array.pop())
                y=int(array.pop())
                array.append(x+y)
            elif elem == "*":
                x=int(array.pop())
                y=int(array.pop())
                array.append(x*y)
            elif elem =="-":
                x=int(array.pop())
                y=int(array.pop())  
                array.append(y-x)
            elif elem == "/":
                x=int(array.pop())
                y=int(array.pop())
                array.append(int(y/x))
            else:
                array.append(int(elem))
        return int(array.pop())