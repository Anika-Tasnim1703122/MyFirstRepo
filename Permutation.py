s = [1,2,3]

def Permutation( arr, start, end):
    if start == end :
        print(str(arr))

    else:
        for i in range(end):
            arr[i],arr[start] = arr[start],arr[i]
            Permutation(arr,start+1,end)
            arr[i],arr[start] = arr[start],arr[i]


Permutation(s,0,(len(s)-1))
