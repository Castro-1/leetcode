def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    aux = 0
    for i in range(m+n-1):
        if nums1[i] == 0:
            nums1[i] = nums2[i-aux]
        elif nums1[i] > nums2[i-aux]:
            nums1[i+1] = nums1[i]
            nums1[i] = nums2[i-aux]
        else:
            aux += 1
    if nums1[-1] == 0:
        nums1[-1] = nums2[-1]
    return nums1


print(merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))
