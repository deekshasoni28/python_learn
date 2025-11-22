X=input()
first=ord(X)
if (65<=first<=90):
    second=first+32
else:
    second=first-32

print(chr(second))
