text=(input())

if "+" in text: 
    left,right=text.split("+")              
    result= int(left)+int(right)
elif "-" in text: 
    left,right=text.split("-")              
    result= int(left)-int(right)
elif "*" in text: 
    left,right=text.split("*")              
    result=int(left)*int(right)
else:
    left,right=text.split("/")              
    result= int(left)//int(right)

print(f'{result}')          
