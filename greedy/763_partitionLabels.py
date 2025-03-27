class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        chars_first_index = {}
        chars_last_index = {}
        results = []
        start = len(s)
        end = 0
        for i in range(len(s)):
            if s[i] not in chars_first_index:
                chars_first_index[s[i]] = i
            else:
                chars_last_index[s[i]] = i
        
        cur =-1
        for key, value in chars_first_index.items():
            if key not in chars_last_index:
                chars_last_index[key] = value
            firstid = value
            lastid = chars_last_index[key]

            if firstid >= end:
                start = firstid
                end = lastid
                results.append(lastid-firstid+1)
                cur +=1
            elif lastid > end:
                end = lastid
                results[cur] = end-start+1
        return results

if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"
    solution = Solution()
    print(solution.partitionLabels(s)) #[9,7,8]