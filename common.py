class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        lst = set()
        lst1 = []
        words[0] = list(words[0])
        words[1] = list(words[1])
        words[2] = list(words[2])
        for i in words[0]:
            if i in words[1] and i in words[2]:
                words[1].remove(i)
                words[2].remove(i)
                lst1.append(i)
        
        return lst1
