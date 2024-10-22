#Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        len1,len2=len(str1),len(str2)
        gcdl=gcd(len1,len2)
        res1=str1[:gcdl]
        res2=str2[:gcdl]
        if(res1==res2):
            return res1
        else:
            return ""
        