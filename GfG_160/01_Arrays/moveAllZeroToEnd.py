# Difficulty: Easy
# Tags: Arrays

# Given an array arr[] of non-negative integers, move all the zeros to the end of the array while maintaining the relative order of the non-zero elements. Perform the operation in place, without using an extra array.

# Examples:

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: The three zeros are moved to the end while the order of the non-zero elements remains unchanged.

# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]
# Explanation: No change in array as there are no 0s.

# Input: arr[] = [0, 0]
# Output: [0, 0]
# Explanation: No change in array as there are all 0s.

# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 105

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def pushZerosToEnd(self, arr: list[int]) -> None:
        count = 0  
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i]
                count += 1