class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result_list = list()
        if not nums:
            return result_list
        
        last_digit = nums[0]
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == last_digit + 1:
                end = nums[i] # extend range
            else:
                # consider the two situations
                # case 1: end of a single digit
                if start == last_digit:
                    result_list.append(str(start))
                # case 2: end of a range
                else:
                    result_list.append(str(start)+"->"+str(end))
                
                # new start
                start = nums[i]
                
            # update last digit
            last_digit = nums[i]
        
        # final number
        if start == last_digit:
            result_list.append(str(start))
        else:
            result_list.append(str(start)+"->"+str(end))
        
        return result_list