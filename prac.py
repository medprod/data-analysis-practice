arr = [4,5,7,11,19]
maxsum = 0
res = []


for i in range(0, len(arr)):
    for j in range(i+2, len(arr)):
        currsum = arr[i] + arr[j]
        if currsum > maxsum:
            maxsum = currsum
            res = [i, j]
        
print(res)

                
            
        
        
    
