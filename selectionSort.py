arr = list() 
while True:
  try:
    num = int(input('set the length of array:'))
  except ValueError:
    print('enter integer only!')
    continue
  else:
    break
for i in range(num):
  while True:
    try:
      n= int(input('num:'))
      arr.append(n)
    except ValueError:
      print('enter integer only!')
      continue
    else:
      break
print(arr)
for i in range(len(arr)):
  min = i
  for j in range(i+1,len(arr)):
    if arr[min]>arr[j]: #find the min value of array
      min = j
  arr[i],arr[min]=arr[min],arr[i] #swap position of min value with a compared value
print(arr)
