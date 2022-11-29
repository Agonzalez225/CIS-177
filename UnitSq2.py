import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
random_points = np.zeros((1000,4))
random_points[:,[0,1]] = np.random.random((1000,2)) * 0.5
x = random_points[:,0]
y = random_points[:,1]
random_points[:,2] = 0.5-random_points[:,0] # distance to horizontal edge of unit square

random_points[:,3] = 0.5-random_points[:,1] # distance to vertical edge of unit square

distanceToCenter       = (x**2 + y**2)**0.5
distanceToEdge = np.min(random_points[:,2:],axis=1)

for radius in np.arange(start=0.01, stop=0.5, step=0.005):
    inCircle = distanceToCenter[distanceToCenter<=radius]
    outCircle   = distanceToEdge[distanceToCenter>radius]
    meanInCircle = round(np.mean(inCircle),3)
    meanOutCircle   = round(np.mean(outCircle),3)
    print(f"r:{round(radius,3)} center:{meanInCircle} edge{meanOutCircle}")

def circle(x, radius = 0.2):
    return ( 0.2**2 - x**2 )**0.5

circleX = np.arange(start=-.2, stop=.2, step=0.005)

fig, ax = plt.subplots()
ax.scatter(x,y,c='black')
ax.scatter(-x,-y,c='black')
ax.scatter(x,-y,c='black')
ax.scatter(-x,y,c='black')
ax.scatter(circleX,circle(circleX),c='red')
ax.scatter(circleX,-circle(circleX),c='red')

ax.plot([-0.5,0.5],[0,0],c='green')
ax.plot([0,0],[-0.5,0.5],c='green')
plt.show()