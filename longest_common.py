class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lst = []
        n = 0
        special = ""
        special1 = ""
        for i in strs:
            n += 1
        for i in strs:
            for j in i:
                lst.append(j)
            break
        for i in lst:
            for x in range(n - 1, -1, -1):
                if i in strs[x] and i not in special:
                    special += i
        for i in special:
            if i in strs[1] and i in strs[2]:
                special1 += i
        return special1
