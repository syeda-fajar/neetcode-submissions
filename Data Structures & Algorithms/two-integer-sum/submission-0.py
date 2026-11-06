class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        result=[]
        for i , number in enumerate(nums):
            need=target-number
            if need not in my_dict:
                my_dict[number]=i
            else:
                result.append(my_dict[need])
                result.append(i)
        return result
                
        