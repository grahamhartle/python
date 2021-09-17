
# mylist = [1,1,3,4,5,5,5,6]
# count = 0
# for i in range(len(mylist)):
#     for k in range(len(mylist)):
#         if i == k :
#             continue
#         elif mylist[i] == mylist[k]:
#             del mylist[k]
#             mylist.append(0)
#             count = count + 1

# print(count)
# print(mylist)

# ls = [1,1,3,4,5,5,5,6]
# result = []
# for item in ls[:]:
#     if item not in result:
#         result.append(item)

# print(result)

mylist = [1,1,3,4,5,5,5,6]
myset = set(mylist)

print(len(mylist) - len(myset))

