class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while (n != 1):
            if n in visit:
                return False
            visit.add(n)
            output = 0
            while n:
                digit = n % 10
                output += digit * digit
                n //= 10
            n = output
        return True