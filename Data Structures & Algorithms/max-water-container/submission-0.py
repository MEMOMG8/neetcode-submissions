class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #make a variable that starts with 0 to save the volume of water
        
        #make two pointers 
            #choose from the two pointers which one has the lowest height 
                #save that lowest height 
                #get the width between right and left index 
                #multiply the lowest height and the width to get the volume of the water
                    #compare the volume of the water with our variable 
                        #if the volume is higher than the variable 
                            #save the variable 
                        #if not 
                            #continue
                            #if left pointer is smaller than right pointer
                                # add one to the pointer
                            #if right pointer is smaller than left pointer 
                                # subtract one to the pointer
                            
            #return variable

        water_volume = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left

            current_volume = height * width
            if current_volume > water_volume:
                water_volume = current_volume
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return water_volume
