class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total = 0
        previous = 0
        for i in s:
            value = roman_values[i]
            if(value>previous):
                total += value - 2*previous
            else:
                total += value
            previous = value
        return total
