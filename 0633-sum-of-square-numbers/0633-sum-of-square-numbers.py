class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        b = int(math.sqrt(c))
        a = 0
        while a <= b:
            temp = a*a + b*b
            
            if temp < c:
                a += 1
            
            elif temp > c:
                b -= 1

            else:
                return True

        return False
        
        