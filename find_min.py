"""153 - Find Minimum in Rotated Sorted Array"""

def product_array(nums):
    if len(nums) == 0:
        return 0

    min_num = nums[0]
    for i in range(1,len(nums)):
        if nums[i] < min_num:
            min_num = nums[i]
    return min_num

if __name__ == "__main__":
    nums = [1,2] 
    print(product_array(nums))