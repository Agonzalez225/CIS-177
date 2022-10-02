

import numpy as np
import pandas as pd
np.random.seed(123)
x = np.random.random(1000)-0.5
np.random.seed(124)
y = np.random.random(1000)-0.5
dist_to_center = (x**2+y**2)**0.5
random_points = pd.DataFrame({'X':x,'Y':y,'Dist To Center':dist_to_center})
quadrants_edges = {1:(0.5,0.5), 2:(-0.5,0.5), 3: (-0.5,-0.5), 4: (0.5,-0.5)}
quadrant_list = []
for xval,yval in zip(x,y):
    quadrant = 0
    if xval>0:
        if yval>0:
            quadrant = 1
        else:
            quadrant = 4
    else:
        if yval>0:
            quadrant = 2
        else:
            quadrant = 3
    quadrant_list.append(quadrant)
random_points['Quadrant'] = quadrant_list

edge_list = []
for quadrant in quadrant_list:
    edge = quadrants_edges[quadrant]
    edge_list.append(edge)

random_points[['Closest Edge X','Closest Edge Y']] = edge_list
random_points['Horizontal Distance to Closest Edge'] = random_points['Closest Edge X'] - random_points['X'] 
random_points['Vertical Distance to Closest Edge'] = random_points['Closest Edge Y'] - random_points['Y']
random_points['Distance to Closest Edge'] = (random_points['Horizontal Distance to Closest Edge']**2+
                            random_points['Vertical Distance to Closest Edge']**2)**0.5
random_points = random_points.sort_values('Dist To Center')
radius_bins = np.arange(start=0.1,stop=0.5,step=0.01)
avg_dist_to_center_list = []
avg_dist_to_nearest_edge_list = []
for radius in radius_bins:
    points_inside_circle = random_points.loc[random_points['Dist To Center']<=radius]
    points_outside_circle= random_points.loc[random_points['Dist To Center']>radius]
    avg_dist_to_center = np.mean(points_inside_circle['Dist To Center'])
    avg_dist_to_center_list.append(avg_dist_to_center)
    avg_dist_to_nearest_edge = np.mean(points_outside_circle['Distance to Closest Edge'])
    avg_dist_to_nearest_edge_list.append(avg_dist_to_nearest_edge)

results_table = pd.DataFrame({'Radius':radius_bins,
    'Avg Dist Center':avg_dist_to_center_list,
    'Avg Dist To Closest Edge':avg_dist_to_nearest_edge_list})
results_table['Difference Between Averages'] = ((results_table['Avg Dist Center']-results_table['Avg Dist To Closest Edge'])**2)**0.5
results_table = results_table.sort_values('Difference Between Averages')
print(f"The best radius is {results_table.iloc[0]['Radius']}")