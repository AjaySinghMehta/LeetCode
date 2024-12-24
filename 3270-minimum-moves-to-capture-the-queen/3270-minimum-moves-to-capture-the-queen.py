# class Solution:
#     def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
#         if a == e and b == f:
#             return 0
#         if a == e or b == f:
#             return 1
#         if abs(a - e) == abs(b - f):
#             return 1
#         if (a + b) % 2 == (e + f) % 2:
#             return 2
#         return 3

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if a==e: # The rook and the queen are in the same column.
            if a!=c: # The bishop is not in the same column.
                return 1
            if (d-b)*(d-f)>0: # The bishop is not between the rook and the queen.
                return 1
        elif b==f: # The rook and the queen are in the same row.
            if b!=d:
                return 1
            if (c-a)*(c-e)>0:
                return 1
        if c+d==e+f: # The bishop and the queen are on the same diagonal.
            if c+d!=a+b:
                return 1
            if (a-c)*(a-e)>0:
                return 1
        elif c-d==e-f: # The bishop and the queen are on the same other diagonal.
            if c-d!=a-b:
                return 1
            if (a-c)*(a-e)>0:
                return 1
        return 2