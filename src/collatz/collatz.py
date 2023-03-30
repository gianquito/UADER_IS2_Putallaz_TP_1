import matplotlib.pyplot as plt

def collatz(num):
    iteraciones = 0
    while num != 1:
        if(num % 2 == 0):
            num = num // 2
        else:
            num = 3*num+1
        iteraciones += 1
    return iteraciones

x = []
y = []
for i in range(1,10000):
    x.append(i)
    y.append(collatz(i))

plt.scatter(x,y)
plt.plot(x,y)
plt.show()