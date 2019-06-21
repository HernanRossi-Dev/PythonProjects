class SubsetSum:
    def __init__(self, inList, value):
        self.rows = len(inList)
        self.cols = self.value = value + 1
        self.inList = sorted(inList)
        self.memoMatrix = [
            [False if x!=0 else self.inList[y] for x in range(0, self.cols)]
            for y in range(0, self.rows)
        ]

    def start(self):
        table = self.memoMatrix
        inList = self.inList
        for i in range(0, self.rows):
            for j in range(1, self.cols):
                entry = inList[i]
                if j - inList[i] > 0:
                    table[i][j] =  table[i-1][j] or table[i-1][j-entry] or entry == j
                else:
                    table[i][j] = table[i-1][j] or entry == j
        return table[-1][-1]

    def printMatrix(self):
        for x in range(0, self.rows):
            print(self.memoMatrix[x])


subsetSum = SubsetSum([4, 6, 10, 1, 3], 23)
subsetSum.start()
subsetSum.printMatrix()
