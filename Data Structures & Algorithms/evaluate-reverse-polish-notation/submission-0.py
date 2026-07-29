class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #create a stack for the operands and the operations

        #make a for loop to check the items in tokens
            #if found an operation
                #return and pop operand b
                #return and pop operand a
                #make math: a operation b
                #push result to stack 
            #else
                #convert character to integer int()
                #push to stack
        #return stack[0] to get the final result

        stack = []
        operations = {"+", "-","*", "/"}
        a = 0
        b = 0
        result = 0

        for c in tokens:
            if c in operations:
                b = stack.pop()
                a = stack.pop()
                if c == "+":
                    result = a + b
                elif c == "-":
                    result = a - b
                elif c == "*":
                    result = a * b
                elif c == "/":
                    result = int(a / b)
                stack.append(result)
            else:
                stack.append(int(c))
        return stack[0]