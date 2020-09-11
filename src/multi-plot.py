import math
import matplotlib.pyplot as plt

d = {
    'k': [1, 1, 1],
}

i = 1
x_len = 4
y_len = math.ceil(len(d) / x_len)

fig = plt.figure(figsize=(x_len * 6, y_len * 5))
for k, v in d.items():
    ax = fig.add_subplot(y_len, x_len, i)
    ax.hist(v, bins=4, density=True, alpha=0.8)
    ax.set_title(k)
    i += 1
