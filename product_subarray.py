"""152 - Maximum Product Subarray"""

def product_array(nums):

        max_prod, min_prod, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            y = min(nums[i], max_prod*nums[i], min_prod*nums[i])            
            max_prod, min_prod = x, y
            ans = max(max_prod, ans)
        return ans

if __name__ == "__main__":
    nums = [2,-5,-2,-4,3]
    print(product_array(nums))