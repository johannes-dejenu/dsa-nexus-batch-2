class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = 0
        m = 0
        o = 0
        moment = True
        for i in matrix:
            o += 1
        for i in matrix:
            for j in i:
                m += 1
            break
        for i in matrix:
            if n + 2 < o:
                continue
            else:
                for j in i:
                    if n + 1 >= o:
                        break
                    else:
                        if j == matrix[n + 1][n + 1]:
                            moment = True
                        else:
                            moment = False
                        n += 1
        return moment
