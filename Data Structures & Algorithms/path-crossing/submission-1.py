class Solution:
    def isPathCrossing(self, path: str) -> bool:
        compass = {"N": (1,0), "S": (-1,0), "W": (0,-1), "E": (0,1)}
        visted = set()
        start = [0,0]
        for direction in path:
            visted.add((start[0], start[1]))
            up, right = compass[direction]
            start[0] += up
            start[1] += right
            if (start[0], start[1]) in visted:
                return True
        return False