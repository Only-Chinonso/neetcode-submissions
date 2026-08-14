class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,m,l,r):
            left,right = arr[l:m],arr[m:r+1]
            i,g,d =l,0,0
            while g < len(left) and d < len(right):
                if left[g] <= right[d]:
                    arr[i] = left[g]
                    g += 1
                else:
                    arr[i] = right[d]
                    d += 1
                i += 1
            if g < len(left):
                arr[i] = left[g]
            if d < len(right):
                arr[i] = right[d]
            return arr

        def mergesort(arr,l,r):
            if l == r:
                return arr
            m = (l + r) // 2
            mergesort(arr,l,m)
            mergesort(arr,m+1,r)
            merge(arr,m,l,r)
        return mergesort(nums,0,len(nums)-1)