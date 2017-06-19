input_array = [20,30]
# with open("C:\integer.txt") as infile:
#    for line in infile:
#       input_array.append(int(line))
start = 0
end = len(input_array)

def Merge(input_array, start, middle, end):
    outputArray = []
    print(start,end=' ')
    print(end,end=' ')

    return outputArray

def Merge_Sort(inp_array, start, end):
    if start < end:
        middle = (start + end) // 2
        print(middle)
        Merge_Sort(inp_array, start, middle)
        Merge_Sort(inp_array, middle + 1, end)
        outputArray = Merge(inp_array, start, middle, end)



outputArray  = Merge_Sort(input_array, 0, len(input_array))
print(outputArray)
