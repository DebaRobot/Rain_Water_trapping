arr = [0,1,0,2,1,0,1,3,2,1,2,1]
class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return len(self.stack) == 0
    def push(self, num):
        return self.stack.append(num)
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack Underflow')
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]
def rainwatertrapping(arr):
    stack = Stack()
    result = []
    maxleft = []
    max1 = 0
    for i in range(len(arr)):
        if stack.isEmpty():
            stack.push(arr[i])
            max1 = max(arr[i], stack.peek())
        elif not stack.isEmpty():
            while(not stack.isEmpty() and stack.peek() > arr[i]):
                 max1 = max(max1,stack.peek())
                 stack.pop()
            maxleft.append(max1)

            stack.push(arr[i])
    return maxleft
def rainwatertrapping1(arr):
    stack = Stack()
    result = []
    maxleft = []
    max1 = 0
    for i in range(len(arr)-1,-1,-1):
        if stack.isEmpty():
            stack.push(arr[i])
            max1 = max(arr[i],stack.peek())
        elif not stack.isEmpty():
            while(not stack.isEmpty() and stack.peek() > arr[i]):
                 max1 = max(max1,stack.peek())
                 stack.pop()
            maxleft.append(max1)

            stack.push(arr[i])
    maxleft.reverse()
    return maxleft

Result = rainwatertrapping(arr)
Result1 = rainwatertrapping1(arr)
water = []
maximum = max(arr)
Result1.insert(0,maximum)
Result.append(maximum)
for i in range(len(arr)):
    water.append(min(Result[i],Result1[i])-arr[i])
print(Result)
print(Result1)
print(sum(water))
