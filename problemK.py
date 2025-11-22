A,B,C=map(int,input().split())

if A>=B and A>=C:
    MAX=A
elif B>=A and B>=C: 
    MAX=B   
else:
    MAX=C   
#MAX= max(A,B,C)

if A<=B and A<=C:
    MIN=A
elif B<=A and B<=C: 
    MIN=B   
else:
    MIN=C
#MIN= min(A,B,C)       

print(f'{MIN} {MAX}')