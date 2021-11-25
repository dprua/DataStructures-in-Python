def merge(a, left, right):  
    i = j = k = 0
    while i < len(left) and j < len(right):   
        if left[i] <= right[j]:
            a[k]=left[i]
            i=i+1
        else:
            a[k]=right[j]
            j=j+1
        k=k+1

    while i < len(left):
        a[k]=left[i]
        i=i+1
        k=k+1

    while j < len(right):
        a[k]=right[j]
        j=j+1
        k=k+1

def sort(a):  
    if len(a)>1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]

        sort(left)
        sort(right)
        
        merge(a, left, right)
