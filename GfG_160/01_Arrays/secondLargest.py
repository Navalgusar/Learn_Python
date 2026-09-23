# Difficulty: Easy
# Tags: Arrays, Searching

# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.

# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.

# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.

# Constraints:
# 2 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 105

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(1)


class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1
            
        first = second = -1
        
        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num 
                
        return second
