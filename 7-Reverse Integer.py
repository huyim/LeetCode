class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        y = ""
        
        for i in range(len(x) - 1, -1, -1):
            y += x[i]
        
        if "-" in y:
            y = y[0:len(y) - 1]
            y = -int(y)
        else:
            y = int(y)
            
        if (y <= (-2)**31 or y >= (2**31 -1)):
            y = 0
        
        return y
