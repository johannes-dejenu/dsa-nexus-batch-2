class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        lst = list(s)
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        
        for i in range(len(s)):
            if s[left] in vowels and s[right] in vowels:
                lst[left], lst[right] = lst[right], lst[left]
                if len(s) == 2:
                    break
                left += 1
                right -= 1
            elif s[left] not in vowels and s[right] not in vowels:
                left += 1
            elif s[left] in vowels and s[right] not in vowels:
                right -= 1
            elif s[left] not in vowels and s[right] in vowels:
                left += 1
           
        return ''.join(lst)
