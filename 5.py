import sys
n = input()
l=len(n)-1
r=0
if n[0]=="0":
    print("no")
    sys.exit()
while r<=l:
    if n[r]!=n[l]:
        print("no")
    r+=1
    l-=1
print("yes")
