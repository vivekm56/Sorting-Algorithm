arr = list()
while True:   #Input type varification
  try:
    num = int(input('set the length of array:'))
  except ValueError:
    print('enter integer only')
    continue
  else:
    break
for i in range(num):
  while True:
    try:
      n = int(input("num:"))
      arr.append(n)
    except ValueError:
      print('enter integer only')
      continue
    else:
      break
print(arr)  
swap = 0
for i in range(1,len(arr)): #Insertion sort starts here
  value = arr[i]            #set value
  j = i-1
  while j >= 0 and value < arr[j]: #Repeat until the condition match
    arr[j+1]=arr[j]    #swap right to left
    j-=1               #compare till the leftmost element
    swap+=1 #swap count
  arr[j+1] = value #Insert element at proper place
print(swap)
print('sorted',arr)#Print sorted array and exit
