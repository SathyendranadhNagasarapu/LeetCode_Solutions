#Link to Question 2125: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self,bank: List[str]) -> int:
        beams=0
        row1=0
        row2=0
        for row in bank:
            if row1==0:
                row1=row.count("1")
                continue
            if row1 and row2:
                beams+=row1*row2
                row1=row2
                row2=0
            row2=row.count("1")
        beams+=row1*row2
        return beams