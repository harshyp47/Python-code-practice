import timeit
arr=[9,2,10,7,1,20,32,4,32]
sl=0
fl=0
tim1=timeit.default_timer()
for i in range(len(arr)):
    if arr[i]>fl:
        sl=fl
        fl=arr[i]
    elif arr[i]>sl and arr[i]!=fl:
        sl=arr[i]
print(sl)
tim2=timeit.default_timer()

print(tim2-tim1)
