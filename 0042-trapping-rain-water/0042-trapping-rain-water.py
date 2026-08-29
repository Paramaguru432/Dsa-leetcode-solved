class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        l,r=0,len(height)-1
        lmx,rmx=height[l],height[r]
        res=0
        while l<r:
            if lmx<rmx:
                l+=1
                lmx=max(lmx,height[l])
                res+=lmx-height[l]
            else:
                r-=1
                rmx=max(rmx,height[r])
                res+=rmx-height[r]
        return res               
        """
        :type height: List[int]
        :rtype: int
        """
        