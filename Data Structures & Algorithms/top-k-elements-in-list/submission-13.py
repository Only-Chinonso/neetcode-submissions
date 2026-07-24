class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}#key(num):value(count)
        for num in nums :
            if num in count :
                count[num] += 1
            else :
                count[num] = 1
        arr = []
        for num,cnt in count.items():
            arr.append([cnt,num])
        arr.sort(reverse=True)
        res = []
        c = 0
        for lst in arr :
            res.append(lst[1])
            c +=1
            if c == k :
                break
        return res
        
