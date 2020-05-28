# Conway's Game of Life is all about simulating real life rules on some random arrangement of cells in a given environment. The rules are as follows.
#
# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation
# Any live cell with two or three live neighbours lives on to the next generation
# Any live cell with more than three live neighbours dies, as if by overpopulation
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
# a for alive
# # for dead later
# x never existed

from random import randint
import numpy as np
def game_of_life(size, generaion_number,matrix,generation_count):
    ### create an empty filed
    if generation_count == None:
        matrix = np.random.randint(2, size =(size ,size ))
        print("at brith:")
        print("\n".join(map(str,matrix)).replace("-2","#").replace("0","x").replace("1","a"))
        generation_count = 0


    # calculate element boundary
    def get_neighbor(i,j,size):
            # normal condition
            if 1 <=  i < size-1 and 1 <= j < size-1 :
                  fate = matrix[i-1][j-1] +  matrix[i-1][j] +  matrix[i-1][j+1]  + \
                         matrix[i][j-1] +                        matrix[i][j+1]  + \
                         matrix[i+1][j-1] +  matrix[i+1][j] +  matrix[i+1][j+1]
            elif 1 >=  i < size-1 and j == size-1 :
                  fate = matrix[i-1][j-1] +  matrix[i-1][1] +  \
                         matrix[i][j-1] +\
                         matrix[i+1][j-1] +  matrix[i+1][1]
            # corner 4
            elif i == size-1 and j == size-1 :
                      fate = matrix[i-1][j-1] +  matrix[i-1][1] +  \
                             matrix[i][j-1]
            # corner 1
            elif i == 0 and j == 0 :
                      fate =                        matrix[i][j+1]    + \
                                matrix[i+1][j+1] +  matrix[i+1][j+1]
            # corner 2
            elif i == 0 and j == size-1:
                  fate = matrix[i][j-1] + \
                         matrix[i+1][j-1] +  matrix[i+1][j]
            #corner 3
            elif i == size-1 and j == 0:
                  fate =  matrix[i-1][j] +  matrix[i-1][j+1]  + \
                                               matrix[i][j+1]
            # top
            elif i == 0 and  0 < j < size-1 :
                      fate = matrix[i][j-1] +               matrix[i][j+1]    + \
                             matrix[i+1][j-1] +  matrix[i+1][j] +  matrix[i+1][j+1]
            elif i == size-1  and 0 < j < size-1 :
                      fate = matrix[i-1][j-1] +  matrix[i-1][j] +  matrix[i-1][j+1]  + \
                             matrix[i][j-1] +                        matrix[i][j+1]
            elif j == 0 and 0 < i < size-1:
                  fate =   matrix[i-1][j] +  matrix[i-1][j+1]  + \
                                             matrix[i][j+1]    + \
                           matrix[i+1][j] +  matrix[i+1][j+1]
            elif j == size-1 and 0 < i < size-1 :
                      fate = matrix[i-1][j-1] +  matrix[i-1][j]  + \
                             matrix[i][j-1]                      +  \
                             matrix[i+1][j-1] +  matrix[i+1][j]
            else: print(i,j)
            return fate


        #reserection
    if generation_count > 1:
        for i in range(0,size):
            for j in range(0,size):
                if get_neighbor(i,j,size) == -6:
                    matrix[i][j] = 1
    print("generate number reserected:",generation_count)
    print("\n".join(map(str,matrix)).replace("-2","#").replace("0","x").replace("1","a"))    # what happens after reserection
        # let's decide the fate
    if generation_count < generaion_number:
        for i in range(0,size ):
            for j in range(0,size ):
                fate = get_neighbor(i,j,size)
                if fate:
                     if fate < 2:
                         matrix[i][j] = -2
                     if fate == 2 or fate == 3:
                         matrix[i][j] = 1
                     if fate > 3:
                          matrix[i][j] =  -2
    else: return



    print("generate number growth",generation_count)
    print("\n".join(map(str,matrix)).replace("-2","#").replace("0","x").replace("1","a"))
    generation_count += 1
    game_of_life(size,generaion_number,matrix,generation_count)

game_of_life(5,2,matrix=None,generation_count=None)
