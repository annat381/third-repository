x = []
y = []
with open ("file3",'r') as f:
    for line in f:
        s=.split(sep=' ')
        x.append(float(s[0]))
        y.append(float(s[1]))

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()