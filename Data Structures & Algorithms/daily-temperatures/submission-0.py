class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                res[prev_i] = index - prev_i
            stack.append(index)
        return res

        #make an array of temp size
        #create a stack for the temperatures

        #make a for loop to check the temperatures
            #while stack AND temp is greated than temp stored at stack
                #pop index off stack
                #calculate current index - popped day index
                #save the output popped day index 

