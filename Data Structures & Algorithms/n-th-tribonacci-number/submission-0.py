class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0,1,1]
        if n < 3:
            return T[n]

        TN = 0
        select = 0
        for i in range(2, n):
            TN = T[0] + T[1] + T[2]
            if select > 2:
                select = 0
            T[select] = TN
            select+=1
        return TN
