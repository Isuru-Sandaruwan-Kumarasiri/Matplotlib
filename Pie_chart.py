from matplotlib import pyplot as plt

category=['food',"transport",'rent',"other"]
cost=[900,850,1400,350]

# plt.pie(cost, labels=category,radius=1.5) # Radious --> increase size of pie chart
# plt.pie(cost, labels=category,radius=1.5,autopct='%0.1f%%')
plt.pie(cost, labels=category,radius=1.5,autopct='%0.1f%%',explode=[0,0,0.2,0])

plt.show()