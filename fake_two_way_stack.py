#Given a string L (of length N) print out every right rotation of L until util it
# reverts to the original string

s=input()
l=len(s)
print(s)
print('\n'.join([s[-x:]+s[:l-x] for x in range(1, l+1)]))