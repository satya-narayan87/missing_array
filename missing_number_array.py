
class Operation(object):
    def missing_array(self, nums, lower, upper):
        """
        Arg: 
        :nums: List[int]
        :lower: int
        :upper: int
        """
        def getRange(lower, upper):
            if lower == upper:
                return "{}".format(lower)
            else:
                return "{}->{}".format(lower, upper)
        ranges = []
        pre = lower - 1
        
        for i in range(len(nums) + 1):
            if i == len(nums):
                cur = upper + 1
            else:
                cur = nums[i]
            if cur - pre >= 2:
                ranges.append(getRange(pre + 1, cur - 1))
                
            pre = cur
            
        return ranges


if __name__ == "__main__":
    # operation 
    input_arr = [0, 1, 3, 50, 75]
    #input_arr = input("input array")
    n = len(input_arr)
    low_range = int(input("Please Enter lower range"))
    high_range = int(input("please Enter higher range"))

    obj = Operation()
    print(obj.missing_array(input_arr,low_range,high_range))

