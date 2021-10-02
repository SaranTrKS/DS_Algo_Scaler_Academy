'''
Equilibrium index of an array
Problem Description

You are given an array A of integers of size N.

Your task is to find the equilibrium index of the given array

Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

NOTE:

Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.



Problem Constraints
1<=N<=1e5
-1e5<=A[i]<=1e5


Input Format
First arugment contains an array A .


Output Format
Return the equilibrium index of the given array. If no such index is found then return -1.


Example Input
Input 1:
A=[-7, 1, 5, 2, -4, 3, 0]
Input 2:

A=[1,2,3]


Example Output
Output 1:
3
Output 2:

-1


Example Explanation
Explanation 1:
3 is an equilibrium index, because: 
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
Explanation 1:

There is no such index.

'''
class Solution:
    # @param A : list of integers
    # @return an integer
    #time complexity O(N),spcae complexity O(N)
    #we can do it in TC:O(N) , SC:O(1)
    def solve(self, A):
        pf = A
        
        for i in range(1, len(A)):
            pf[i] += pf[i-1]
        
        if pf[len(A) -1] ==0:
            return 0
        for i in range(1,len(A)):
            if pf[i-1] == pf[len(A)-1] - pf[i]:
                return i
        return -1
