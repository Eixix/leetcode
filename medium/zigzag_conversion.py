import unittest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [["" for _ in range(len(s))] for _ in range(numRows)]

        if numRows == 1:
            return s

        ascending = True
        rowNumber = 0
        columnNumber = 0

        for letter in s:
            matrix[rowNumber][columnNumber] = letter

            if rowNumber < numRows - 1 and ascending:
                rowNumber += 1
            elif rowNumber > 0 and not ascending:
                rowNumber -= 1
                columnNumber += 1
            elif rowNumber <= 0 and not ascending:
                rowNumber += 1
                ascending = True
            elif rowNumber >= numRows - 1 and ascending:
                ascending = False
                rowNumber -= 1
                columnNumber += 1

        to_return = ""

        for i in range(numRows):
            to_return += "".join(matrix[i])

        return to_return


class Test(unittest.TestCase):
    solution = Solution()

    def test1(self):
        self.assertEqual(self.solution.convert(
            "PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test2(self):
        self.assertEqual(self.solution.convert(
            "PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test3(self):
        self.assertEqual(self.solution.convert(
            "A", 1), "A")


if __name__ == "__main__":
    unittest.main()
