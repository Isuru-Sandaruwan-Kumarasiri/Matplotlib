from matplotlib import pyplot as plt

##   Line Chart

plt.figure()

age =[23,34,24,25,64,53,45]
weight=[38,55,45,71,43,55,65]

plt.subplot(1,2,1)
plt.plot(age,weight,'r--')
plt.title("BMI")
plt.xlabel("Age")
plt.ylabel("Weight")



##   Bar chart

plt.subplot(1,2,2)
subjects=['maths','physics','chemistry']
marks=[70,80,55]

plt.barh(subjects,marks)# horizontal
# plt.bar(subjects,marks,width=0.4) # vertical
plt.title("Student Marks")
plt.xlabel("Subject")
plt.ylabel("Marks")


# Display the plot
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()