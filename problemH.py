A,B = map(int,input().split())
import math
div=A/B
floor_val =math.floor(div)
ceil_val=math.ceil(div)
round_val=math.floor(div+0.5)
print(f'floor {A} / {B} = {floor_val}')
print(f'ceil {A} / {B} = {ceil_val}')
print(f'round {A} / {B} = {round_val}')