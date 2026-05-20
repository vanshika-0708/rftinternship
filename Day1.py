#given list
data=[10,None,20,10,"",30,None,40]
#empty list for cleaned data
clean_list=[]
#counter for removed values
removed_count=0
for item in data:
    if item is None or item=="":
        removed_count+=1
        continue
    if item not in clean_list:
        clean_list.append(item)
    else:
        removed_count+=1
clean_list.sort
print("original list:",data)
print("cleaned list:",clean_list)
print("Total Removed values:",removed_count)        