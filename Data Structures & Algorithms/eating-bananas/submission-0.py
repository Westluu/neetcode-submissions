class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_k = 0
        while l <= r:
            print(f"r: {r}")
            print(f"l: {l}")
            k = int(l + ((r - l) // 2))
            print(k)
            time = 0
            for p in piles:
                time += math.ceil(p / k)

            if time <= h:
                min_k = k
                r = k - 1
            else:
                l = k + 1
        return min_k


            

        