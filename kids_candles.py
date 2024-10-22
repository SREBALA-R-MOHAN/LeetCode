#There are n kids with candies. 
# You are given an integer array candies, 
# where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

#Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, 
# or false otherwise.


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        arr=[]
        max=candies[0]
        for i in candies:
            if(i > max):
                max=i
        for i in candies:    
            if(i+extraCandies >= max):
                arr.append(True)
            else:
                arr.append(False)
        return arr
            