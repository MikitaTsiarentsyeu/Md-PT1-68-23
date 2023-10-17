ls = [1,2,3,4,5,6,7,8,9]

def search(l, target, low=0, high=None):
    if high == None:
        high = len(l)-1
    if low > high:
        return -1
    mid = (low+high)//2
    if l[mid] == target:
        return mid
    elif l[mid] > target:
        return search(l, target, low, mid-1, mid)
    else:
        return search(l, target, mid+1, high, mid)
    
print(search(ls,5))
