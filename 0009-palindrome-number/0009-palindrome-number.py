class Solution:
    def isPalindrome(self, x: int) -> bool:
        #some edge cases:
        if x<0:
            return False
        if x == 0:
            return True
        if x%10 == 0:
            return False

        # first method is converting the integer to string and comparing it
        # x = str(x)
        # if x == x[::-1]:
        #     return True
        # return False

        # second method is to use another variable and reverse it
        lastDigit = 0 
        reverse = 0
        a = x
        while a>0:
            lastDigit = a%10
            reverse = reverse *10 + lastDigit
            a = a//10
        return (x == reverse)