class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """ filter = lambda nums_list,elements_count: nums_list[(len(nums_list) - elements_count):]          
        nums1 = sorted(filter(sorted(nums1),m) + filter(sorted(nums2),n)) """
        a = m-1
        b = n-1
        c = m+n-1
        while c >= 0:
            if b == -1:
                # First Condition
                pass
            elif a == -1:
                #  Second Condition
                nums1[c] = nums2[b]
                b -= 1
            elif nums2[b] > nums1[a]:
                # Third Condition
                nums1[c] = nums2[b]
                b -= 1
            elif nums1[a] > nums2[b]:
                # Fourth Condition
                nums1[c] = nums1[a]
                a -= 1
            else:
                # Fifth Condition
                nums1[c] = nums1[a]
                a -= 1
            c -= 1