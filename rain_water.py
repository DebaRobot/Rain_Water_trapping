
arr = [0,1,0,2,1,0,1,3,2,1,2,1]
stack = []
us = []
mx =  arr[0]
for i in range(len(arr)):
  if(len(stack) == 0):
    stack.append(arr[i])
  elif(len(stack) != 0 and arr[i] > mx):
    mx =  max(mx, arr[i])
    stack.append(mx)
  else:
    mx =  max(mx, arr[i])
    stack.append(mx)


my = arr[-1]
for i in range(len(arr)-1, -1, -1):
  if(len(us) == 0):
    us.append(my)
  elif(len(stack) != 0 and arr[i] > my):
    my =  max(my, arr[i])
    us.append(my)
  else:
    us.append(my)
us.reverse()

final = []
for k,j in zip(stack, us):
  final.append(min(j,k))

result = []
for i in range(len(final)):
  result.append(final[i] -  arr[i])
print(sum(result))
print(stack)
print(us)
