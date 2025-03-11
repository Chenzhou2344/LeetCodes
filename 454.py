class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = {}
        for n1 in nums1:
            for n2 in nums2:
                sum12 = n1+n2
                if sum12 in hashmap:
                    hashmap[sum12]+=1
                else:
                    hashmap[sum12]=1
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                hashval = -(n3+n4)
                if hashval in hashmap:
                    count += hashmap[hashval]

        return count