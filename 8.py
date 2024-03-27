n = input()
names = []

for i in range(int(n)):
    names.append(input())

for i in range(1,len(names)):
    for j in range(i-1,-1,-1):
        print(f"{names[i]}:salam {names[j]}!")

for i in range(len(names)):
    print(f"{names[i]}:khodafez bacheha!")
    for j in range(i+1,len(names)):
        print(f"{names[j]}:khodafez {names[i]}!")

