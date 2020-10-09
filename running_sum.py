"""1480 - Running sum of 1d Array"""

def running_sum(a):
    b = [a[0]]
    s = len(a)
    for i in range(0, s):
        if i > 0:
            b.append(a[i])
            a[i] = sum(b)
    return a

if __name__ == '__main__':
    a = [1,2,3,4]
    print(running_sum(a))