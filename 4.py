import matplotlib.pyplot as plt

n=0
a=1.4
b=0.3
x_n=0
x_m=0
y_n=0
y_m=0
x_1=[]
x_2=[]
y_1=[]
y_2=[]
while n<1000:
	x_m=y_n+1-a*x_n**2
	x_1.append(x_n)
	x_2.append(x_m)
	x_n=x_m
	y_m=b*x_n
	y_1.append(y_n)
        y_2.append(y_m)
	y_n=y_m
	n +=1
x_3=[]
x_4=[]
y_3=[]
y_4=[]
n=0
a=1.07
b=0.5
x_n=0
y_n=0
y_m=0
x_m=0
while n<1000:
	x_m=y_n+1-a*x_n**2
        x_3.append(x_n)
        x_4.append(x_m)
        x_n=x_m
        y_m=b*x_n
        y_3.append(y_n)
        y_4.append(y_m)
        y_n=y_m
	n +=1

plt.scatter(x_1,x_2,label='x, a=1.4, b=0.3')
plt.scatter(y_1,y_2,label='y, a=1.4, b=0.3')
plt.scatter(x_3,x_4,label="x, a=1.07, b=0.5")
plt.scatter(y_3,y_4,label="y, a=1.07,b=0.5")
plt.legend()
plt.savefig("4-3.pdf")
