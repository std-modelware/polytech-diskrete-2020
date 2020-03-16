
import matplotlib.pyplot as plot
from matplotlib.patches import RegularPolygon
import numpy as np
import matplotlib.markers as marker

def get_poly_points(n, r=1):
    x = []
    y = []
    angle = np.pi - (n-2) * np.pi / n
    for i in range(n):
        x.append(r * np.cos(i * angle))
        y.append(r * np.sin(i * angle))
    return x, y


def enlarge_num(number, digits):
    tmp = number << digits
    tmp = tmp | number
    return tmp

def count_sym_axis(number, digits):
    mask_len = digits // 2
    mask = 2 ** mask_len - 1
    mask1 = mask << (2 * digits - mask_len)
    mask2 = mask << digits
    number = enlarge_num(number, digits)
    counter = 0
    for i in range(digits - 1):
        piece1 = number & mask1
        piece2 = number & mask2
        piece1 = piece1 >> (mask_len + 1)
        if piece1 == piece2:
            counter += 1
        mask1 = mask1 >> 1
        mask2 = mask2 >> 1
    return counter



x, y = get_poly_points(3)
print(x, '\n', y)
#kek = marker.MarkerStyle(marker=None, fillstyle=None)
plot.scatter(x, y, c='w', edgecolors='k')
plot.show()