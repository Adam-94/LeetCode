"""238 - Product of Array Except Self"""

def product_array(nums):
        ans = [1 for _ in nums]
        
        left = 1
        right = 1
        
        for i in range(len(nums)):
            ans[i] *= left
            ans[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]
        return ans

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    print(product_array(nums))