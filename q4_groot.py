




def findPies(arr,n):
    def recfindpies(start, n, temp, sum):



        if n == sum:
            res.append(temp)

            raise TypeError(temp)
        elif start== len(arr) or n < sum:
            return
        else:
            # dynamic variable call
            for i in range(start,len(arr)):
                recfindpies(i+1, n, temp + [i], sum + arr[i])



    try:
        for i in range(len(arr)):
            recfindpies(i+1, n, [i],arr[i])
    except TypeError as temp:
        return temp




#4. Groot's pie finder
res=[]

res= findPies([1, 2, 3, 2, 1], 6)
print(res)
