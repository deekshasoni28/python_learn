X=int(input())
temp=X
 
while (temp>=10):
    temp=temp//10

#first_digit= int(X[0])
#aagr first_digit divide hoga 2 se toh even else odd
 
if (temp%2==0):        
    print('EVEN')    
else:             
    print('ODD')    
