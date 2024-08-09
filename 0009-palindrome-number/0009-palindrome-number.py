class Solution:
    def isPalindrome(self, x: int) -> bool:
        # first method is converting the integer to string and comparing it
        x = str(x)
        if x == x[::-1]:
            return True
        return False