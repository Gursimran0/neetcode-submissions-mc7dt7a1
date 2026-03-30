import statistics
class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        res = [0]*(m+n)
        i=0
        j=0
        k=0
        while m>j and n>k:
            if nums1[j]<nums2[k]:
                res[i]=nums1[j]
                i+=1
                j+=1
            else:
                res[i]=nums2[k]
                i+=1
                k+=1
        
        while m>j:
            res[i]=nums1[j]
            i+=1
            j+=1
        while n>k:
            res[i]=nums2[k]
            i+=1
            k+=1
        r=statistics.median(res)
        return r



        
    
        