#Jerron Jones
#Dutch flag sorting program homework from practice.geeksforgeeks.org
n=5
arr = [2, 1, 0, 1, 0, 2]
class Solution:
    def sort012(self,arr,n):
        start=0
        middle=0
        end=n-1
    
        while middle <= end: #If the number is 0, it swaps to the start pointer. Then the start and middle pointer move up 1
            if arr[middle]==0:
                arr[middle] , arr[start] = arr[start] , arr[middle]
                middle+=1
                start+=1
            
            elif arr[middle]==1: #if the number is 1, the middle pointer moves up one.
                middle+=1
            
            else:
                arr[middle] , arr[end] = arr[end] , arr[middle] #if the number is two, the element swaps places with the number at the high pointer.
                end-=1
newarray = Solution()
newarray.sort012(arr,n)             
print(arr)
