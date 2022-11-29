def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    ans = []
    hashmap = {}
    for i in range(len(nums1)):
        if nums1[i] in hashmap:
            hashmap[nums1[i]] += 1
        else:
            hashmap[nums1[i]] = 1

    for i in range(len(nums2)):
        if nums2[i] in hashmap:
            if hashmap[nums2[i]] != 0:
                ans += [nums2[i]]
                hashmap[nums2[i]] -= 1

    return ans


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))
