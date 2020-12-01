# Space O(n)
def square (arr):
    squared = []
    for i in range(len(arr)):
        sum = arr[i] * arr[i]
        squared.append(sum)

    return squared

# Space O(n)
def sum (num):
    if num <= 0:
        return num

    return num + sum(num-1)

# Runtime O(1)
def push (self, data):
    node = StackNode(data)
    node.next = self.top
    self.top = node
    self.size += 1

# Runtime O(log(n))
def targetIndex (arr, target):
    left = 0
    right = len(arr)
    index = int(right / 2)

    while left <= right:
        if arr[index] == target:
            return index

        if arr[index] < target:
            left = index + 1
        else:
            right = index - 1

        index = (right - left) // 2 + left

    return -1

# Runtime O(n)
def find (self, item):
    node = self.root

    while node:
        if node.data == item:
            break

    node = node.next

    return node

# Runtime O(n*log(n))
def mergeSort (arr, startIndex, endIndex):
    if startIndex != endIndex:
        middle = int((startIndex + endIndex) / 2)
        mergeSort(arr, startIndex, middle)
        mergeSort(arr, middle+1, endIndex)
        return merge(arr, startIndex, arr[startIndex:middle+1], arr[middle+1:endIndex+1])

def merge (arr, index, left, right):
    leftStart = 0
    leftEnd = len(left) - 1
    rightStart = 0
    rightEnd = len(right) - 1

    while leftStart <= leftEnd and rightStart <= rightEnd:
        if left[leftStart] < right[rightStart]:
            arr[index] = left[leftStart]
            leftStart += 1
        else:
            arr[index] = right[rightStart]
            rightStart += 1

        index += 1

    while leftStart <= leftEnd:
        arr[index] = left[leftStart]
        leftStart += 1
        index += 1

    while rightStart <= rightEnd:
        arr[index] = right[rightStart]
        rightStart += 1
        index += 1

    return arr

# Runtime O(n²)
def bubbleSort(arr):
    count = 1

    while count < len(arr):
        for i in range(len(arr) - count):
            c = arr[i]
            n = arr[i + 1]

        if c > n:
            temp = c
            arr[i] = n
            arr[i + 1] = temp

        count += 1

    return arr

# Runtime O(2ⁿ)
def fib(n: int) -> int:
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

# Runtime O(n!)
def permutations(head, tail=''):
    if len(head) == 0:
        print(tail)
    else:
        for i in range(len(head)):
            permutations(head[:i] + head[i+1:], tail + head[i])
