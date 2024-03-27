from collections import defaultdict

n = int(input())
markersDict = defaultdict(int)
for i in range(n):
    marker = int(input())
    markersDict[marker]+=1

sortedMarker =dict(sorted(markersDict.items()))
print(min(sortedMarker,key=sortedMarker.get))
