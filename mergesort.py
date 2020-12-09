def merge(a,start,mid,end):
    start2 = mid+1
    #breaks early if no need to sort
    if(a[mid] <= a[start2]):
        return

    while(start <= mid and start2 <= end):
        if(a[start] <= a[start2]):
            start += 1
        else:
            i = start2
            v = a[start2]
            while(i!=start):
                a[i] = a[i-1]
                i -= 1
            a[start] = v

            start+=1
            mid+=1
            start2+=1

def mergesort(a,start,end):
    if(start < end):
        mid = ((end-start)//2) + start
        mergesort(a,start,mid)
        mergesort(a,mid+1,end)
        merge(a,start,mid,end)
    return