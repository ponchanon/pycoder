class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        n = len(arr)
        prefix_max = arr[:]
        suffix_min = arr[:]
        
        for i in range(1,n):
            prefix_max[i] = max(prefix_max[i],prefix_max[i-1])
            suffix_min[n-i-1] = min(suffix_min[n-i-1], suffix_min[n-i])
        print(prefix_max)
        print(suffix_min)
        for i in range(n):
            if i==0 or suffix_min[i]>=prefix_max[i-1]:
                chunks +=1
        return chunks
        
        