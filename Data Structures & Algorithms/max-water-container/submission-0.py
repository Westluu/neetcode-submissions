class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Input: An array of ints, where each ith value represents the height bar
        #Output: The maximum amount of water a container can hold

        #The amount of water a container can hold is equivalent to the area 
        #between 2 height in heights

        #Where Area = min(height[i], height[j]) * abs(i-j)
        
        #Algo:
            #Since we are finding 2 points (most likely far apart on oppsite ends)
            #Initial thought is its a 2 pointer problem

            #l and r, where l = 0, r = len(heights) - 1
            #we start wide and can shift of container through out
            #keeping track of the largest area
        
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            max_area = max(max_area, area)
            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        return max_area




        