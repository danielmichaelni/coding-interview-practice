"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity
should be O(log(m+n)).

Problem provided by: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

def find_median(nums1, nums2):
    total_len = len(nums1) + len(nums2)
    if total_len % 2 == 0:
        return (
            find_kth(total_len // 2, nums1, nums2) +
            find_kth((total_len // 2) - 1, nums1, nums2)
        ) / 2
    return find_kth(total_len // 2, nums1, nums2)

def find_kth(k, nums1, nums2):
    if len(nums1) == 0:
        return nums2[k]
    if len(nums2) == 0:
        return nums1[k]

    mid1 = len(nums1) // 2
    mid2 = len(nums2) // 2
    if k > mid1 + mid2:
        if nums1[mid1] > nums2[mid2]:
            return find_kth(k - mid2 - 1, nums1, nums2[mid2 + 1:])
        else:
            return find_kth(k - mid1 - 1, nums1[mid1 + 1:], nums2)
    else:
        if nums1[mid1] > nums2[mid2]:
            return find_kth(k, nums1[:mid1], nums2)
        else:
            return find_kth(k, nums1, nums2[:mid2])

def find_median_optimized(nums1, nums2):
    total_len = len(nums1) + len(nums2)
    if total_len % 2 == 0:
        return (
            find_kth(total_len // 2, nums1, 0, len(nums1), nums2, 0, len(nums2)) +
            find_kth((total_len // 2) - 1, nums1, 0, len(nums1), nums2, 0, len(nums2))
        ) / 2
    return find_kth(total_len // 2, nums1, 0, len(nums1), nums2, 0, len(nums2))

def find_kth_optimized(k, nums1, start1, end1, nums2, start2, end2):
    if end1 <= start1:
        return nums2[start2 + k]
    if end2 <= start2:
        return nums1[start1 + k]

    mid1 = start1 + (end1 - start1) // 2
    mid2 = start2 + (end2 - start2) // 2
    if k > (mid1 - start1) + (mid2 - start2):
        if nums1[mid1] > nums2[mid2]:
            return find_kth(k - (mid2 - start2) - 1, nums1, start1, end1, nums2, mid2 + 1, end2)
        else:
            return find_kth(k - (mid1 - start1) - 1, nums1, mid1 + 1, end1, nums2, start2, end2)
    else:
        if nums1[mid1] > nums2[mid2]:
            return find_kth(k, nums1, start1, mid1, nums2, start2, end2)
        else:
            return find_kth(k, nums1, start1, end1, nums2, start2, mid2)

print(find_median([1, 3], [2]) == 2)
print(find_median([1, 2], [3, 4]) == 2.5)
print(find_median([1, 1, 1], [1, 1, 1]) == 1)
print(find_median([1, 2, 2], [1, 2, 3]) == 2)

"""
                                     k on right half             k on left half
                               ___________________________ ____________________________
                              |                           |                            |
mid of nums1 > mid of nums2   | eliminate left half nums2 | eliminate right half nums1 |
                              |___________________________|____________________________|
                              |                           |                            |
mid of nums1 <= mid of nums2  | eliminate left half nums1 | eliminate right half num2  |
                              |___________________________|____________________________|

... (mid of nums1) ...|... (mid of nums2) ...
                      ^
                     mid
... (mid of nums1) ...|... (mid of nums2) ...
                      ^
                     mid
"""
