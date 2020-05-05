#Array formation starts here as per input
arr = list()
num = int(input("Set the length of array:"))
print("Enter number in array")
for i in range(num):
  n = int(input("num:"))
  arr.append(n)
print("Arr",arr) 
#Concept of bubbleSort starts here 
c=0
for i in range(len(arr)-1):#Take the length of array for sat the number of steps for comparison
        for j in range(0, len(arr)-i-1):#Here we sat number of swap
            if arr[j] > arr[j+1]:# compare the values of array
                arr[j], arr[j+1] = arr[j+1], arr[j]#swap or manage array's values in order
                c+=1
print("swapCount = ",c)#count number of swap
print("Sorted Arr",arr)#Print sorted array 
