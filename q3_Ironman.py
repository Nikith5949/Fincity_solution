

# 3. Ironman's legacy in trouble


# allocates extra memory dynamically
def allocate(ln,arr):
    arr.extend([0]*(ln-len(arr)+1))




def findTheRange(n,rnge):
    a = [0]*(n+1)

    for i in rnge:

        if i[0]<len(a) and i[1] < len(a):
            a[i[0]] +=i[2]
            a[i[1]] -=i[2]

        else:
            allocate(i[1],a)

    sum =0
    ma = 0
    index =-1
    count=0
    for i in range(0,len(a)):

        sum+=a[i]
        a[i]=sum
        if sum>=ma:
            ma = sum
            count+=1
            index=i
        else:
            count=0


    return([index,index+count+1,ma])














# 3. Ironman's legacy in trouble-4pts

#list itself is mutable in python unlike java can allocate more elements(so do not require new Data Structure)

res=findTheRange(5, [[2, 4, 5], [1, 3, 6], [2, 4, 7]])

print(res)