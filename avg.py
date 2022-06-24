from math import log, e
import matplotlib.pyplot as plt
import numpy as np

with open("values.txt", "r") as f:
    inputdata = [float(x) for x in f.readlines()]
out = [log(x, e) for x in inputdata]

#for val in out: 
    #print(val)

figure, axis = plt.subplots(1,2)
plt.get_current_fig_manager().set_window_title('Discharging Capacitor')

x = np.array([x * 10 for x in range(19)])
y1 = np.array(out)
axis[0].plot(x,y1)
axis[0].set_title("ln Data")
axis[0].set_ylabel("ln volts / v")
axis[0].set_xlabel("time / secs")


y2 = np.array(inputdata)
axis[1].plot(x,y2)
axis[1].set_title("Raw Data")
axis[1].set_ylabel("volts / v")
axis[1].set_xlabel("time / secs")

plt.show()
