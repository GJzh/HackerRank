#RAMESH CHANDRA

import math
x = [15 , 12 , 8  , 8 ,  7 ,  7 ,  7 ,  6   , 5  , 3]
y = [10  ,25 , 17  ,11 , 13 , 17 , 20 , 13 , 9  , 15]
sum_x,sum_y=0,0
for i in xrange(len(x)):
    sum_x,sum_y=sum_x+x[i],sum_y+y[i]
mean_x = float(sum_x)/len(x)
mean_y = float(sum_y)/len(y)
A, B , C = 0,0,0;
for i in xrange(len(x)):
    A += (x[i]-mean_x)*(y[i]-mean_y)
    B += (x[i]-mean_x)**2
    C += (y[i]-mean_y)**2
ans = float(A)/math.sqrt(B*C)
print ans
