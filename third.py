
# arr=[0,-1,2,-3,1]
# arr=[1, -2, 1, 0, 5]
arr=[0, 2, -2, 5, 3, -8]

def triplets(arr):
    n=len(arr)
    triplet=[]
    arr.sort()
    # print(arr)
    for i in range(n-2):
        left = i+1
        right = n-1
        x = arr[i]
        # print(left,right,x)
        while(left<right):
            if x + arr[left] + arr[right] == 0:
                triplet.append([x,arr[left],arr[right]])
                left += 1
                right -= 1
            elif x + arr[left] + arr[right] < 0:
                left += 1
            else:
                right -= 1
        
    return triplet
    
arr2 = triplets(arr)
for i in arr2:
    print(i)

