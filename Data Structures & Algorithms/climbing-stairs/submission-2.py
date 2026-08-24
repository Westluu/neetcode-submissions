class Solution:
    def climbStairs(self, n: int) -> int:
        #input: n steps
        #output: how many distinct ways can we reach n steps by going 1 or 2
        
        #we can always reach n by going 1 n times
        #so output is at least 1

        #there is always 2 decisions to choose from, either go up 1 or up 2
        #to reach 2, we can up 1 twice of 2 oce, making the output 2

        #while to go 3, we can go up 1 trice, up 2 then 1, or up 1 twice then 2
        prev, cur = 1, 2
        if n <= 2:
            return n
        for i in range(3, n):
            temp = cur
            cur = prev + cur
            prev = temp
        
        return prev + cur

        



        