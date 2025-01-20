from matplotlib import pyplot as plt

#Histogram means it is used to find count or sum etc in  specific range 

marks=marks=[70,80,55,45,78,54,34,90,23,34,32,67]
# default range are 10 by 10
# plt.hist(marks,bins=6)
# plt.hist(marks,bins=[0,50,75,100]) #cutermize the bins size
# plt.hist(marks,bins=[0,50,75,100],rwidth=0.95)
plt.hist(marks,bins=[0,50,75,100],rwidth=0.95,color='g')
plt.show()