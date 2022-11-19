import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
random_points = np.zeros((1000,4))
random_points[:,[0,1]] = np.random.random((1000,2)) * 0.5
x = random_points[:,0]
y = random_points[:,1]
random_points[:,2] = 0.5-random_points[:,0]
random_points[:,3] = 0.5-random_points[:,1]

dist_to_center       = (x**2 + y**2)**0.5
dist_to_nearest_edge = np.min(random_points[:,2:],axis=1)

for radius in np.arange(start=0.01, stop=0.5, step=0.005):
    center_dist = dist_to_center[dist_to_center<=radius]
    edge_dist   = dist_to_nearest_edge[dist_to_center>radius]
    avgdistcenter = round(np.mean(center_dist),3)
    avgdistedge   = round(np.mean(edge_dist),3)
    print(f"r:{round(radius,3)} center:{avgdistcenter} edge{avgdistedge}")

def circle(x, radius = 0.2):
    return ( 0.2**2 - x**2 )**0.5

def circle_bottom(x, radius = 0.2):
    return -( 0.2**2 - x**2 )**0.5

fig, ax = plt.subplots()
ax.scatter(x,y,c='black')
ax.scatter(-x,-y,c='black')
ax.scatter(x,-y,c='black')
ax.scatter(-x,y,c='black')
ax.scatter(x,circle(x),c='red')
ax.scatter(-x,circle(-x),c='red')
ax.scatter(x,-circle(x),c='red')
ax.scatter(-x,-circle(-x),c='red')
ax.plot([-0.5,0.5],[0,0],c='green')
ax.plot([0,0],[-0.5,0.5],c='green')
plt.show()