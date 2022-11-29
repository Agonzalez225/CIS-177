
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anmtn

np.random.seed(123)
#create 400 random numbers, the numbers <.4 make them living cells, >.4 make them dead
board = np.array(np.random.random((20,20))<0.4,dtype=int)
print(f"The number of live cells is {np.sum(board)}") #sum means counting

def tick(board):

    neighbors   = np.zeros(shape=board.shape)#create same shaped board
    next_generation = np.zeros(shape=board.shape) #create a board of all DEAD cells

    #left edge
    for row in np.arange(start=1, stop=board.shape[0]-1):
        subarray = board[row-1:row+2,:2]
        neighbors[row,0] = np.sum(subarray) - board[row,0]#count the LIVING neighbors
        if board[row,0]: #is this edge cell currently alive? is it a 1?
            if neighbors[row,0] in [1,2]: #1: Any live cell with one or two ALIVE neighbors survives.
                next_generation[row,0] = 1
        else: #it is a 0, currently dead
            if neighbors[row,0] in [2,3]: #2: Any dead cell with two or three ALIVE neighbors becomes a live
                next_generation[row,0] = 1
    #right edge [row,-1]
    for row in np.arange(start=1, stop=board.shape[0]-1):
        subarray            = board[row-1:row+2,-2:]
        neighbors[row,-1]   = np.sum(subarray) - board[row,-1] #counting the ALIVE neighbors
        if board[row,-1]:#check if cell is currently alive
            if neighbors[row,-1] in [1,2]: #1: Any live cell with one or two ALIVE neighbors survives.
                next_generation[row,-1] = 1 #stays alive
        else:
            if neighbors[row,-1] in [2,3]: #2: Any dead cell with two or three ALIVE neighbors becomes a live
                next_generation[row,-1] = 1#becomes alive
    #top edge
    for column in np.arange(start=1, stop=board.shape[1]-1):
        subarray            = board[:2,column-1:column+2]
        neighbors[0,column] = np.sum(subarray) - board[0, column]#count LIVING neighbors
        if board[0,column]:#is cell currently alive or 1?
            if neighbors[0,column] in [1,2]: #1: Any live cell with one or two LIVING neighbors survives.
                next_generation[0,column] = 1 #stays alive
        else:#is cell currently dead?
            if neighbors[0,column] in [2,3]: #2: Any dead cell with two or three LIVING neighbors becomes a live
                next_generation[0,column] = 1 #becomes alive

    #bottom edge
    for column in np.arange(start=1, stop=board.shape[1]-1):
        subarray                = board[-2:,column-1:column+2]
        neighbors[-1,column]    = np.sum(subarray) - board[-1, column]#count the LIVING neighbors
        if board[-1,column]:#is cell currently aa 1?
            if neighbors[-1,column] in [1,2]: #1: Any live cell with one or two live neighbors survives.
                next_generation[-1,column] = 1#survives
        else:#is cell currently dead a 0?
            if neighbors[-1,column] in [2,3]: #2: Any dead cell with two or three live neighbors becomes a live
                next_generation[-1,column] = 1#becomes alive

    #corner rules
    neighbors[0,0]      = np.sum(board[:2,:2]) - board[0,0]     #top left corner
    if neighbors[0,0]: next_generation[0,0] = 1#Any live or dead cell with any live neighbors is alive in the nxt stage.
    neighbors[0,-1]     = np.sum(board[:2,-2:]) - board[0,-1]   #top right corner
    if neighbors[0,-1]:next_generation[0,-1] = 1 #Any live cell with any live neighbors survives.
    neighbors[-1,-1]    = np.sum(board[-2:,-2:]) - board[-1,-1] #bottom right corner
    if neighbors[-1,-1]:next_generation[-1,-1] = 1#Any live cell with any live neighbors survives.
    neighbors[-1,0]     = np.sum(board[-2:,:2]) - board[-1,0]   #bottom left corner
    if neighbors[-1,0]:next_generation[-1,0] = 1#Any live cell with any live neighbors survives.

    #inner cells

    for row in np.arange(start=1, stop=board.shape[0]-1):
        for column in np.arange(start=1, stop=board.shape[1]-1):
            subarray = board[row-1:row+2, column-1:column+2]
            neighbors[row,column] = np.sum(subarray) - board[row, column] #counting the living neighbors
            #general rules:
            if board[row, column]: #is the cell a 1 currently alive?
                if neighbors[row,column] in [2,3]:
                    next_generation[row,column] = 1 #any live cell with 2 or 3 live neightobrs survives
            else:                                   #is the cell a 0? is cell currently dead
                
                if neighbors[row,column] == 3:      #any dead cell with 3 neighbors
                    next_generation[row,column] = 1 #becomes a live cell
    return neighbors, next_generation

ticks   = [board]
alive   = [np.sum(board)]

max_tick = 100
seconds_per_tick = 0.01

'''
for _ in range(max_tick):
    neighbors, board = tick(ticks[-1])
    ticks.append(board)
    alive.append(np.sum(board))
'''

fig,ax = plt.subplots(ncols=2)
im = ax[1].imshow(ticks[0], cmap='Reds', vmin=0, vmax=1)
ax[1].set_xlabel('Red means Alive, \n White Means Dead')
fig.colorbar(im)
#https://brushingupscience.com/2016/06/21/matplotlib-animations-the-easy-way/
ax[0].set(xlim=(0,max_tick), ylim=(0,400))
ax[0].set_ylabel('Number of Living Cells')
alive_counter = ax[0].plot([],[])[0]

#https://stackoverflow.com/questions/17212722/matplotlib-imshow-how-to-animate
#https://stackoverflow.com/questions/42621036/how-to-use-funcanimation-to-update-and-animate-multiple-figures-with-matplotlib
def animate_func(i):
    if i == 0:
      del ticks[1:]
      del alive[1:] #blue line counting the # of living cells
    im.set_array(ticks[-1])
    ax[1].set_title('Tick '+str(i))
    neighbors, board = tick(ticks[-1])
    ticks.append(board)
    alive.append(np.sum(board))
    alive_counter.set_data(range(len(alive)),alive)
    return [alive_counter,im] #[im]

anim = anmtn.FuncAnimation(fig, animate_func, frames = max_tick, interval = seconds_per_tick*1000)
plt.show()


print()