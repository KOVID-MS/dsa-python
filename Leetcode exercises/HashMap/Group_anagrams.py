class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            if tuple(count) not in  dic.keys():
                dic[tuple(count)] = []
            dic[tuple(count)].append(s)
        
        return dic.values()