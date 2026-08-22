class NumArray:

    def __init__(self, nums: List[int]):
        self.pref=[]
        curr=0
        for i in nums:
            curr+=i
            self.pref.append(curr)
        

    def sumRange(self, left: int, right: int) -> int:
        rightsum=self.pref[right]
        leftsum=self.pref[left-1] if left>0 else 0
        return rightsum-leftsum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)