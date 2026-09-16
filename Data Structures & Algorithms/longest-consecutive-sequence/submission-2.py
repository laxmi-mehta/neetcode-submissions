class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum = set(nums)
        longest = 0
        for num in setnum:
            if num - 1 not in setnum:
                count = 1
                current = num

                while current + 1 in setnum:
                    count += 1
                    current += 1

                longest = max(longest, count)

        return longest
