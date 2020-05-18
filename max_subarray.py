"""53 - Maximum Subarray - Kadane's algorithm"""

def product_array(nums):
        n = len(nums)

        for i in range(1,n):
            print(i-1)
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

if __name__ == "__main__":
    nums = [-1,-6,-2,-4,-8,-1]
    print(product_array(nums))