#Jerron Jones
#M03 Binary seach program
#used to find what index a certian number can be found in
n = 5
arr = [1, 2, 3, 4, 5]
k = 4

class Solution:	
    def binarysearch(self, arr, n, k):
        start = 0
        end = n - 1
    
        while start <= end: 
            middle = (start + end) // 2 #places a pointer at the middle of the remaining part of the array
            
            if arr[middle] < k: #moves the starting pointer one past the middle
                start = middle + 1
            
            elif arr[middle] > k: #moves the pointer one below the middle
                end = middle - 1
            
            else:
                return middle

solution = Solution()
index = solution.binarysearch(arr, n, k)
print(index)
