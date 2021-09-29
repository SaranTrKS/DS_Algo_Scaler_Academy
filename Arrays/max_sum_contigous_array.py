'''
Max Sum Contiguous Subarray
Problem Description

Find the contiguous subarray within an array, A of length N which has the largest sum.



Problem Constraints
1 <= N <= 1e6
-1000 <= A[i] <= 1000



Input Format
The first and the only argument contains an integer array, A.



Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.



Example Input
Input 1:

 A = [1, 2, 3, 4, -10] 
Input 2:

 A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 


Example Output
Output 1:

 10 
Output 2:

 6 


Example Explanation
Explanation 1:

 The subarray [1, 2, 3, 4] has the maximum possible sum of 10. 
Explanation 2:

 The subarray [4,-1,2,1] has the maximum possible sum of 6. 
'''

###Solution

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        ### sliding window solution with O(n**2) time complexity
        # curr_max = -1e6
        
        # for i in range(1,len(A)+1):
        #     curr_sum = 0
        #     for j in range(i):
        #         curr_sum += A[j]
                
        #     if curr_sum > curr_max:
        #         curr_max = curr_sum
            
        #     for k in range(1,len(A)-i+1):
        #         curr_sum -= A[k -1]
        #         curr_sum += A[i+k-1]
                
        #         if curr_max < curr_sum:
        #             curr_max = curr_sum
                
        # return curr_max
        
        #kadane's algorithm or dynamic_programming approach O(N)
        
        kd_arr = []
        kd_arr.append(A[0])
        for i in range(1,len(A)):
            kd_arr.append(max(kd_arr[i-1]+A[i], A[i]))
        return max(kd_arr)
