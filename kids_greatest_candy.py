"""1431 - Kids With the Greatest Number of Candies"""

def candy(a, candies):
    m = max(a)
    for i, n in enumerate(a):
        if n + candies >= m:
            a[i] = True
        else:
            a[i] = False

if __name__ == '__main__':
    a = [2,3,5,1,3]
    candies = 3
    print(candy(a, candies))