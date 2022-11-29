def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    count = 0
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            nums.append("_")
            i -= 1
            count += 1
        i += 1
    return len(nums)-count


removeElement([3, 2, 2, 3], 3)
