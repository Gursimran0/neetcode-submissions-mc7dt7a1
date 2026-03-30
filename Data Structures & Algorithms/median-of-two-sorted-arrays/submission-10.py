class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sm=nums1
        lg=nums2
        if len(sm)>len(lg):
            sm,lg = lg,sm
        total = len(sm)+len(lg)
        half = total//2
        
        l=0
        r=len(sm)-1

        while True:
            i = (l+r)//2
            j = half-i-2
            smLeft = sm[i] if i>=0 else float("-infinity")
            smRight = sm[i+1] if (i+1)<len(sm) else float("infinity")
            lgLeft = lg[j] if j>=0 else float("-infinity")
            lgRight = lg[j+1] if (j+1)<len(lg) else float("infinity")

            if smLeft<=lgRight and lgLeft<=smRight:
                if total%2==1:
                    return min(lgRight,smRight)
                
                return ((max(smLeft,lgLeft)+min(smRight,lgRight))/2)
            elif smLeft>lgRight:
                r=i-1
            else:
                l=i+1
        
            
