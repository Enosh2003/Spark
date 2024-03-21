numbers=(list(eval(input("enter integers:"))))
target=int(input("enter the target value:"))
outlist=[]
for item in numbers:
  pair=set()
  complement=target-item
  if complement in numbers:
    pair.update((item,complement))
    outlist.append(pair)
print(outlist)