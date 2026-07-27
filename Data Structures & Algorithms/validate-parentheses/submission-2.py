class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hash_map = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in hash_map:
                if stack and stack[-1] == hash_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

        #we have string s consisting of ('(', ')', '{', '}', '[' and ']')
        
        #make a stack to save the each character we see when we loop
        #make a hash map to pair each key (closing bracket) with a value (open bracket)

        #make a for loop going through every character 'c' in the string 's'
            #check if the c is a key in the hash map
                #if so, we check if there is a stack and if the last item in the stack equals the value in the hashmap
                    #if so, we take the last item in the stack
                #if the character c is not a key in the hash map
                    #return false
            #if c is not a key in the hash map it is a value so
                #we append it in the stack
        #return true if the is not stack meaning the stack is empty 
        #else return false   