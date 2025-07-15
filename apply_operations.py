class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = 0
        for i in nums:
            if n + 1 > len(nums) - 1:
                break
            if nums[n] == nums[n + 1]:
                nums[n] *= 2
                nums[n + 1] = 0
            n += 1
        num = []
        zero = []
        for i in nums:
            if i == 0:
                zero.append(i)
            else:
                num.append(i)
        return num + zero
