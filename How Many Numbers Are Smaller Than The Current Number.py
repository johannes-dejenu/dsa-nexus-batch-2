class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        size = len(nums)
        lst = []
        for i in range(size):
            mini = nums[i]
            n = 0
            for j in range(size):
                if mini > nums[j]:
                    n += 1
            lst.append(n)
        return lst
