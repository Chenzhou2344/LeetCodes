class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for s in magazine:
            if s in hashmap:
                hashmap[s]+=1
            else:
                hashmap[s] = 1
        for t in ransomNote:
            if t in hashmap:
                hashmap[t]-=1
                if hashmap[t]<0:
                    return False
            else:
                return False
        return True