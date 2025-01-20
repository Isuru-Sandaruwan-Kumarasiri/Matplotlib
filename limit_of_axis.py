from matplotlib import pyplot as plt
import numpy as np

x=[1, 2, 3, 4]

plt.plot(x,np.power(x,2),color='r',marker='^',linestyle=':',linewidth=1)
plt.plot(np.power(x,2),np.power(x,3),color='b',marker='o',linestyle='-',linewidth=1)
# left,right=plt.xlim() # this return exists right and left limit
# left,right=plt.xlim(2,7) # give specific range for lef and right limits
# left,right=plt.xlim(2) # default  change left side
# left,right=plt.xlim(right=5) # to change right limit ,we must give as parameter
left,right=plt.xlim(left=1,right=5)
bottom,top=plt.ylim(0,5)
print(left)
print(right)
plt.xlabel("number of elements")
plt.ylabel("enargy of data")
plt.title("data science")
plt.show()

