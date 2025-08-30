import matplotlib.pyplot as plt

x = [i for i in range(10)]
print(x)

y = [2*i for i in range(10)]
print(y)

# plt.plot(x, y)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("Correlation of y-x")

plt.scatter(x,y)
plt.show()
