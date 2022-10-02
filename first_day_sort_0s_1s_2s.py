# Python program to sort an array with
# 0, 1 and 2 in a single pass

# Function to sort array
def sort012(a,arr_size):
    low=0
    mid=0
    high=arr_size-1
    while mid<=high:
        if a[mid]==0:
            a[low],a[mid]=a[mid],a[low]
            low+=1
            mid+=1
        elif a[mid]==1:
            mid+=1
        else:
            a[mid],a[high]=a[high],a[mid]
            high-=1
    return a

