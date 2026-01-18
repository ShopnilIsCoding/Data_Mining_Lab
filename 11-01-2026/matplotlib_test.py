import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y,marker = 'o')

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.title("Sports Watch Data")
plt.grid()
plt.show()


import matplotlib.pyplot as plt2
import numpy as np2

#day one, the age and speed of 13 cars:
x = np2.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np2.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt2.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np2.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np2.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt2.scatter(x, y)

plt2.show()

cars = ["BMW", "Volvo", "Ford", "Audi", "Toyota"]
sales = [23, 17, 35, 29, 40]

plt.figure()
plt.bar(cars, sales)
plt.xlabel("Car Brand")
plt.ylabel("Units Sold")
plt.title("Car Sales")
plt.show()

speed = np.array([60, 62, 65, 70, 72, 75, 78, 80, 85, 90, 95, 100])

plt.figure()
plt.hist(speed)
plt.xlabel("Speed")
plt.ylabel("Frequency")
plt.title("Speed Distribution")
plt.show()

labels = ["TCP", "UDP", "ICMP", "HTTP"]
traffic = [45, 30, 15, 10]

plt.figure()
plt.pie(traffic, labels=labels, autopct="%1.1f%%")
plt.title("Network Traffic Share")
plt.show()
