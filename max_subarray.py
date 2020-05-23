def product_array(nums):
        n = len(nums)

        for i in range(1,n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

if __name__ == "__main__":
    nums = [-1,2,4,-4,8,1]
    print(product_array(nums))