num = input("Please enter a number").strip() 
if num.isdecimal():
    num = int(num)
else:
    print("This is not a valid number, sir ")
    exit()




numlist = list(range(1,num+1))

biglist =[]

for i in numlist:
    smalllist=[]
    for x in numlist:
        smalllist.append(" {} X {} = {}".format(x, i, x*i))
        biglist.append(smalllist)
   


print(biglist)
    


