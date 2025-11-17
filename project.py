def printtwoOdd(arr,size):
    a = arr[0]
    x = 0
    y = 0
    setbit = 0
    for i in range(1,size):
        a = a^arr[i]
    setbit = a &~(a-1)
    for i in range(size):
        if(arr[i] & setbit):
            x = x^arr[i]
        else:
            y = y^arr[i]
    print("The two odd occurring numbers are",x,y)
arr = []
size = int(input("Enter the size of the array"))
for i in range(0,size):
    z = int(input("Enter the element"))
    arr.append(z)
printtwoOdd(arr,size)