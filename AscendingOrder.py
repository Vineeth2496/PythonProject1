list1=[2,9,5,6,10,12,3,5]
print(list1)
for i in range(0, len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i]<=list1[j]:
            list1[i],list1[j] = list1[j], list1[i]
print(list1)
