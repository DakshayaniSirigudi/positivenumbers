list1=[0,0,0,0,0]
list2=[0,0,0,0,0]
print("enter any 5 numbers: ")
i=0
while i<5:
    list1[i]=input("enter:")
    i=i+1
print("The input list is: ")
list1=list(map(int,list1))
print(list1)
print("The output list is: ") 
i=0
while i<5:
  if list1[i]>0:
     list2[i]=list1[i]
  i=i+1
print(list2)
print("done")
