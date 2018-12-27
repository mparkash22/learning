import numpy as np
np.random.seed(123)
ourtcomes=[]
for x in range(10):
    coin=np.random.randint(0,2)
    if coin == 0 :
        ourtcomes.append("head")
    else :
        ourtcomes.append("tails")
print(ourtcomes)