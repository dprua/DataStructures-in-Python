def sort(a):
    for i in range(1, len(a)):  # start from 1 since 1st element is trivially sorted
        ivalue = a[i]
        j = i
        while j > 0 and a[j - 1] > ivalue:  
            a[j] = a[j - 1]
            j = j - 1
        a[j] = ivalue
        
if __name__ == '__main__':
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("before:", a)
    sort(a)
    print(" after:", a)