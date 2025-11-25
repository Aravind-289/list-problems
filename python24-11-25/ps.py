" sorted"
k=[10,11,12]
is_sorted=True
for x in range(len(k)):
    for y in range(x+1,len(k)):
        if k[x]>k[y]:
            is_sorted=False
            break
if is_sorted:
    print("list is sorted")
else:
    print("list is not sorted")

" convert 2D to 1D list"
k=[[10,20,30],[40,50,60]]
tem=[]        #[10,20,30,40,50,60]
for x in k:    #x=[10,20,30]
    for y in x:   # y=10   [10,20,30]   [40,50,60]
       tem+=[y]
print(tem)

# " total"
j=[[10,20,30],50,60,[70,80,90]]
tem=[]
for x in j:
    if type(x)==list:
        tem.extend(x)
    
    else:
        tem.append(x)
print(tem)
        
#two list convert into combination of tuple
a=[10,20,30]
b=[100,200,300]
res=[]
for x,y in zip(a,b):
   res.append((x,y))
print(res)    

#
a=[]
b=[]
h=[(10, 100), (20, 200), (30, 300)]
for x in h:
    for y in range(len(x)):
        if y==0:
            a.append(x[y])
        else:
            b.append(x[y])
print(a)
print(b)

#
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
# for x in matrix:
#     sum1=0
#     for y in x:
#         sum1+=y


# adding first indexcing  postions
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
tem=[]
for x in range(len(matrix)):
    sum1=0
    for y in range(len(matrix[x])):
        sum1+=matrix[y][x]
    tem.append(sum1)
print(tem)
        