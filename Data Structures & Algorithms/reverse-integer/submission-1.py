class Solution:
    def reverse(self, x: int) -> int:
        a=""
        k=""
        for i in str(x):
            if i.isdigit():
                k+=str(i)
            else:
                a+=str(i)
        q=int(a+k[::-1]) 
        if q > -2147483648  and  q<2147483647:
            return q
        return 0