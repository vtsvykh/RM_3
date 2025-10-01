Q = 100
Price = 10
VC = 5
FC = 300
rD = 0.1
A = 1000
L = 0
tax = 0.2

Q1 = 80
Q2 = 100
Q3 = 120
p1 = 0.3
p2 = 0.3
p3 = 0.4
a = (P-VC) / (A * (1 - L)) * (1 - tax)
b = -FC - rD * (A * L) / (A * (1 - L)) * (1 - tax)
y1 = a * x1 + b
y2 = a * x2 + b
y3 = a * x3 + b
Ey = y1 * p1 + y2 * p2 + y3 * p3
sy = ((Ey - y1)**2 * p1 + (Ey - y2)**2 * p2 + (Ey - y3)**2 * p3) ** 0.5

p_y2_y3 = p2 + p3
ymin = Ey - 3 * sy
ymax = Ey + 3 * sy

def u(y, p):
  sum = 0
  for i in range(len(y)):
    if y[i] > 0:
      sum += y[i] ** 0.5 * p[i]
    else:
      sum += -abs(y[i]) ** 0.5 * p[i]
  return sum

F = a * Ey - b * sy**2
Eu = u([y1, y2, y3], [p1, p2, p3])
print(Eu)

V = [p1, p2 + p3]
r = [1, 2]
R = V[0] * r[0] + V[1] * r[1]
print(R)

from scipy import stats
stats.norm.cdf(-1,75)
