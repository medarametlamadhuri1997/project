a=[1,2,3,4,5,6,7,8,7,6,7]
b=""
len=len(a)
for i in range(0,len):
    if i in range(0,len-1):
        str_num=str(a[i])
        b=b+str_num+","
    else:
        str_num = str(a[i])
        b = b + str_num
print(b)
c=b[:-3]+b[-1]
print(c)


