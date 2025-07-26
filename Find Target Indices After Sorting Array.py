class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        lst = []
        n = 0
        for i in range(1, size):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        for i in nums:
            if i == target:
                lst.append(n)
            n += 1
        return lst
        
