n = int(input())
nums = []
for i in range(n):
    nums.append(float(input()))

print("max: {:.3f}".format(max(nums)))
print("min: {:.3f}".format(min(nums)))
print("avg: {:.3f}".format(sum(nums)/len(nums)))
