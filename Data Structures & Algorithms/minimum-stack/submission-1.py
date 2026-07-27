class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minimumStack[-1] if self.minimumStack else val)
        self.minimumStack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minimumStack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumStack[-1]
        
#understand the problem: it ask us to create a class that supports different operations

    #minstack initializes the stack object 
        #initialize it by creating two stacks
    
    #create the push operation
        #in our first stack we append the value val
        #set val to the minimum value between the actual value and the value in the minimum stack value we create
        #after choosing the minimum value we append that into the minimum stack to keep trace of it

    #create the pop operation
        #we take out the last item in the self stack
        #get rid of the last minimum value in the minimum stack

    #create top operation
        #we just return the top value in the stack

    #create get min operation
        #return the top value in the minimum stack   