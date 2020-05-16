"""1 - Two Sum"""
def two_sum(nums, target):
      for i, num in enumerate(nums):
        if target-num in nums and i!=nums.index(target-num):
            return [nums.index(target-num), i]

if __name__ == '__main__':
    nums = [3,2,3]
    target = 6
    print(two_sum(nums, target))