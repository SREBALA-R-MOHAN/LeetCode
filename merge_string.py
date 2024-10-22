#You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
#Return the merged string.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        for i in range(len(word1)):
            res= res+""+word1[i]
            if(len(word2)>i):
                for j in range(i,i+1):
                    res= res+""+word2[j]
                if(i==len(word1)-1 and len(word1)<len(word2)):
                    for k in range(j+1,len(word2)):
                        res=res+""+word2[k]
        return res


            

        

