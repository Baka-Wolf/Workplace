import numpy as np
import matplotlib.pyplot as plt
Pro=0.02
N=100000000
total=0         #六星总数
s=0
u=[]            #记录出货位置
number=[]

for i in range(N):
    x=np.random.uniform(0,1)
    if x<Pro:
        total=total+1
        Pro=0.02
        u.append(s+1)
        s=0

    else:
        s=s+1
        if s>50:
            Pro=Pro+0.02

for i in range(1,101):
    number.append(100*u.count(i)/total)

print(number)

plt.bar(range(1,101),number,color='green',width=0.5)
plt.title('Where the top operator is?')
plt.xlabel('Number')
plt.ylabel('Probability(%)')
plt.show()