"""217 - Contains Duplicate"""

def contains_duplicate(nums=[]):
       if len(nums) == len(set(nums)):
            return False
       else:
            return True

if __name__ == "__main__":
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(contains_duplicate(nums))
