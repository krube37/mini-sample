n = int(input("Enter number of elements : "))  
li = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]  
print("List is - ", li)
l = len(li)
s = 0
count = 1
r = 1
maxi = li[0]+li[1]-1
x = 0
for i in range(l):
    s = s + li[i]
    for j in range(r,l):
        tempsum = s
        s = s + li[j]
        if(s > maxi):
            b = j
            a = i
            x = a
            maxi = s
        if(s == maxi and a < i and b < j):
            b = j
    r += 1
    s = 0
print(li[a:b+1])
print(maxi)
            
            



