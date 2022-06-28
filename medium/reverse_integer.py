import unittest


class Solution:
    def reverse(self, x: int) -> int:
        reverse_number = int(str(abs(x))[::-1])
        reverse_number = reverse_number if x > 0 else -reverse_number
        return reverse_number if reverse_number >= -pow(2, 31) and reverse_number <= (pow(2, 31) - 1) else 0


class Test(unittest.TestCase):
    solution = Solution()

    def test1(self):
        self.assertEqual(self.solution.reverse(1231534236469), 0)


if __name__ == "__main__":
    unittest.main()
