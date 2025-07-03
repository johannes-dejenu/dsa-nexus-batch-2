class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = 0
        y = x
        z = x
        while x > 0:
            x //= 10
            n += 1
        num_of_digits = n - 1
        new = 0
        while y > 0:
            rem = y % 10
            res = rem * 10 ** (num_of_digits)
            new += res
            y //= 10
            num_of_digits -= 1
        if new == z:
            return bool(new == z)
        else:
            return bool(new == z)
