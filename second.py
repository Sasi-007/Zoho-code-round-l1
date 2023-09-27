
arrays=[[1,20],[19,30],[40,70]]

def rooms(arrays):
    if not arrays:
        return 0
    
    starttime = sorted([interval[0] for interval in arrays]) 
    endtime = sorted([interval[1] for interval in arrays])
    room=0
    end=0
    
    for start in starttime:
        # print(start,endtime[end])
        if start < endtime[end]:
            room += 1
        else:
            end += 1
    
    return room
# print(arrays[0][1])
res = rooms(arrays)
print(res)
