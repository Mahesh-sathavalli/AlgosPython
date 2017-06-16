input_array = [9,8,7,6,5,4,3,2,1,98,74,67,20,1020,45,34,56,2242,6767,32542,7756,234,
               123,45,6546,645,12,453,566,234,56,234,565,343,2356,767,453,3434,53242,
               1234,54546,466454,123,45,53,343,534,345,656512,12321]
#with open("C:\integer.txt") as infile:
#    for line in infile:
#       input_array.append(int(line))
start = 0
end = len(input_array)

def Merge(input_array,start,middle,end):
    leftEnd=middle - start +1
    rightEnd = end-middle
    left= []
    right = []
    for i in range(0,leftEnd):
        left.append(input_array[i])
        print(left[i],end=' ')
    for i in range(0,rightEnd):
        right.append(input_array[i])
        print(right[i],end = ' ')
        
    


    
def Merge_Sort(input_array,start,end):
    if start < end:
        middle = (start + end)//2
        Merge_Sort(input_array,start,middle)
        Merge_Sort(input_array,middle+1,end)
        Merge(input_array,start,middle,end)

Merge_Sort([20,10],0,len([20,10]))
