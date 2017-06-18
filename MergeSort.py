input_array = [20,30,40,10,50]
# with open("C:\integer.txt") as infile:
#    for line in infile:
#       input_array.append(int(line))
start = 0
end = len(input_array)

def Merge(input_array, start, middle, end):
    leftEnd = middle - start
    rightEnd = end - middle
    left = []
    right = []
    outputArray = []
    if leftEnd == 0:
        left.append(input_array[0])
    for i in range(0, leftEnd):
        left.append(input_array[start + i ])
    for i in range(0, rightEnd):
        right.append(input_array[middle +1+ i])
    lefti = 0
    righti = 0
    totali = 0

    while lefti < len(left) and righti < len(right):
        if left[lefti] <= right[righti]:
            outputArray.append(left[lefti])
            lefti = lefti+1
        else:
            outputArray.append(right[righti])
            righti = righti+1
    while lefti < len(left):
        outputArray.append(left[lefti])
        lefti = lefti + 1
    while righti < len(right):
        outputArray.append(right[righti])
        righti = righti +1

    return outputArray

def Merge_Sort(inp_array, start, end):
    if start < end:
        middle = (start + end) // 2
        Merge_Sort(inp_array, start, middle)
        Merge_Sort(inp_array, middle + 1, end)
        outputArray = Merge(inp_array, start, middle, end)



outputArray  = Merge_Sort(input_array, 0, len(input_array))
print(outputArray)
