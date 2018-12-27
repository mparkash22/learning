import masterdata as md
import numpy as np

# print (md.areas)
# for a in range(20):
#     print(a)


#loop a disctionary
europe = md.europe_with_cap
for key,value in europe.items() :
    print("the capital of "+key +" is "+ value)


for a in md.np_height:
    print(str(a) + " inches")


for a in np.nditer(md.np_2d) :
    print(a)