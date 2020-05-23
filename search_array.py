"""33 - Search in Rotated Sorted Array"""

def search_array(nums, target):
    if not nums:
        return -1

    find = nums[0]
    get_index = 0

    for i,j in enumerate(nums):
        if target == j:
            return i
    
    return -1

if __name__ == "__main__":
    target = 0
    nums = [[],5]
    print(search_array(nums,target))