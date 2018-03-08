from AutoPyBejeweled import makeMove

def findMove(Rows):
    print "in findmove function"
    foundMove = False
    #SearchFiveInARow(Rows)
    
    #SearchFourInARow(Rows)
    searchForAThree(Rows)
    


def SearchFiveInARow(Rows):
    for x in range(8):
        for y in range(8):
            #move up
            #check up
            if y>4:
                x1 = x
                y1 = y-2
                x2 = x
                y2 = y-3
                y3 = y-4
                y4 = y-5
                if(y2 >= 0):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x1][y3]  == Rows[x1][y4]):
                        print('found 5 move at',x,y,'moving up up')
                        makeMove((x,y),(x,y-1))
                        break
            #check left
            
            if x>4:
                x1 = x-1
                x2 = x-2
                y1 = y-1
                y2 = y-1
                x3 = x-3
                x4 = x-4
                if(x2 >= 0 and y2 >= 0):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x3][y2]  == Rows[x4][y2]):
                        print('found 5 move at',x,y,'moving up left')
                        makeMove((x,y),(x,y-1))
                        break
            #check right
            if x < 3:
                x1 = x+1
                x2 = x+2
                y1 = y-1
                y2 = y-1
                x3 = x+3
                x4 = x+4
                if(x2 <= 7 and y2 >= 0):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x3][y2] == Rows[x4][y2]):
                        print('found 5 move at',x,y,'moving up right')
                        makeMove((x,y),(x,y-1))
                        break
            #check around            
            x1 = x+1
            x2 = x-1
            y1 = y-1
            y2 = y-1
            x3 = x-2
            x4 = x+2
            if(x4 <= 7 and x2 >= 0 and y2 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x3][y2]  == Rows[x4][y2]):
                    print('found 5 move at',x,y,'moving up around')
                    makeMove((x,y),(x,y-1))
                    break
            #move left
            #check up
            if y>4:
                x1 = x-1
                y1 = y-1
                x2 = x-1
                y2 = y-2
                y3 = y-3
                y4 = y-4
                if(y2 >= 0 and x1 >= 0):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x2][y3]  == Rows[x2][y4]):
                        print('found move at',x,y,'moving left up')
                        makeMove((x,y),(x-1,y))
                        break
            #check left
            if x >4:
                x1 = x-2
                x2 = x-3
                y1 = y
                y2 = y
                x3 = x-4
                x4 = x-5
                if(x2 >= 0):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x3][y2] == Rows[x4][y2]):
                        print('found 5 move at',x,y,'moving left left')
                        makeMove((x,y),(x-1,y))
                        break
            
            #check down
            if y<3:
                x1 = x-1
                x2 = x-1
                y1 = y+1
                y2 = y+2
                y3 = y+3
                y4 = y+4
                if(x2 >= 0 and y4 <= 7):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x2][y3]  == Rows[x2][y4]):
                        print('found move at',x,y,'moving left down')
                        makeMove((x,y),(x-1,y))
                        break 
            #check around
            x1 = x-1
            x2 = x-1
            y1 = y+1
            y2 = y-1
            y3 = y+2
            y4 = y-2
            if(x2 >= 0 and y3 <= 7 and y4 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x2][y3] == Rows[x2][y4]):
                    print('found move at',x,y,'moving left around')
                    makeMove((x,y),(x-1,y))
                    break 
            #move right
            #check up
            if y>4:
                x1 = x+1
                y1 = y-1
                x2 = x+1
                y2 = y-2
                y3 = y-3
                y4 = y-4
                if(y4 >= 0 and x1 <= 7):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x2][y3] == Rows[x2][y4]):
                        print('found move at',x,y,'moving right up')
                        makeMove((x,y),(x+1,y))
                        break
            #check right
            if x<3:
                x1 = x+2
                x2 = x+3
                y1 = y
                y2 = y
                x3 = x+4
                x4 = x+5
                if(x4 <= 7):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x3][y2] == Rows[x4][y2]):
                        print('found move at',x,y,'moving right right')
                        makeMove((x,y),(x+1,y))
                        break
            #check down
            if y<3:
                x1 = x+1
                x2 = x+1
                y1 = y+1
                y2 = y+2
                y3 = y+3
                y4 = y+4
                if(x2 <= 7 and y4 <= 7):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x2][y3]  == Rows[x2][y4]):
                        print('found move at',x,y,'moving right down')
                        makeMove((x,y),(x+1,y))
                        break
            #check around
            x1 = x+1
            x2 = x+1
            y1 = y+1
            y2 = y-1
            y3 = y+2
            y4 = y-2
            if(x2 <= 7 and y3 <= 7 and y4 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x2][y3]  == Rows[x2][y4]):
                    print('found move at',x,y,'moving right around')
                    makeMove((x,y),(x+1,y))
                    break
            #move down
            #check down
            x1 = x
            y1 = y+2
            x2 = x
            y2 = y+3
            y3 = y+4
            y4 = y+5
            if(y4 <= 7):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x2][y3]  == Rows[x2][y4]):
                    print('found move at',x,y,'moving up up')
                    makeMove((x,y),(x,y+1))
                    break
            #check left
            if x>4:
                x1 = x-1
                x2 = x-2
                y1 = y+1
                y2 = y+1
                x3 = x-3
                x4 = x-4
                if(x4 >= 0 and y2 <=7):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x3][y2] == Rows[x4][y2]):
                        print('found move at',x,y,'moving up left')
                        makeMove((x,y),(x,y+1))
                        break
            #check right
            if x <3:
                x1 = x+1
                x2 = x+2
                y1 = y+1
                y2 = y+1
                x3 = x+3
                x4 = x+4
                if(x4 <= 7 and y2 <= 7):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x3][y2]  == Rows[x4][y2]):
                        print('found move at',x,y,'moving up right')
                        makeMove((x,y),(x,y+1))
                        break
            #check around
            x1 = x+1
            x2 = x-1
            y1 = y+1
            y2 = y+1
            x3 = x+2
            x4 = x-2
            if(x3 <= 7 and 42 >= 0 and y2 <= 7):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x3][y2] == Rows[x4][y2]):
                    print('found move at',x,y,'moving up around')
                    makeMove((x,y),(x,y+1))
                    break

def SearchFiveLShape(Rows):
    for x in range(8):
        for y in range(8):
            #move left
            x1 = x-2            
            x2 = x-3
            y1 = y-2
            y2 = y-3
            y3 = y-4
            if(y2 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x1][y3]):
                    print('found 4 move at',x,y,'moving up up')
                    makeMove((x,y),(x,y-1))
                    break
    
def SearchFourInARow(Rows):
    for x in range(8):
        for y in range(8):
            #move up
            #check up
            if y>3:
                x1 = x
                y1 = y-2
                x2 = x
                y2 = y-3
                y3 = y-4
                if(y2 >= 0):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x1][y3]):
                        print('found 4 move at',x,y,'moving up up')
                        makeMove((x,y),(x,y-1))
                        break
            #check left
            
            if x>3:
                x1 = x-1
                x2 = x-2
                y1 = y-1
                y2 = y-1
                x3 = x-3
                if(x2 >= 0 and y2 >= 0):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x3][y2]):
                        print('found 4 move at',x,y,'moving up left')
                        makeMove((x,y),(x,y-1))
                        break
            #check right
            if x < 4:
                x1 = x+1
                x2 = x+2
                y1 = y-1
                y2 = y-1
                x3 = x+3
                if(x2 <= 7 and y2 >= 0):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x3][y2]):
                        print('found 4 move at',x,y,'moving up right')
                        makeMove((x,y),(x,y-1))
                        break
            #check around            
            x1 = x+1
            x2 = x-1
            y1 = y-1
            y2 = y-1
            x3 = x-2
            x4 = x+2
            if(x4 <= 7 and x3 >= 0 and y2 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x3][y2]):
                    print('found 4 move at',x,y,'moving up around')
                    makeMove((x,y),(x,y-1))
                    break
                elif(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] ==  Rows[x4][y2]):
                    print('found 4 move at',x,y,'moving up around')
                    makeMove((x,y),(x,y-1))
                    break
                
            #move left
            #check up
            if y>3:
                x1 = x-1
                y1 = y-1
                x2 = x-1
                y2 = y-2
                y3 = y-3
                if(y2 >= 0 and x1 >= 0):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x2][y3]):
                        print('found 4 move at',x,y,'moving left up')
                        makeMove((x,y),(x-1,y))
                        break
            #check left
            if x >3:
                x1 = x-2
                x2 = x-3
                y1 = y
                y2 = y
                x3 = x-4
                if(x2 >= 0):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x3][y2]):
                        print('found 4 move at',x,y,'moving left left')
                        makeMove((x,y),(x-1,y))
                        break
            
            #check down
            if y<4:
                x1 = x-1
                x2 = x-1
                y1 = y+1
                y2 = y+2
                y3 = y+3
                if(x2 >= 0 and y3 <= 7):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x2][y3] ):
                        print('found 4 move at',x,y,'moving left down')
                        makeMove((x,y),(x-1,y))
                        break 
            #check around
            x1 = x-1
            x2 = x-1
            y1 = y+1
            y2 = y-1
            y3 = y+2
            y4 = y-2
            if(x2 >= 0 and y3 <= 7 and y4 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x2][y3]):
                    print('found 4 move at',x,y,'moving left around')
                    makeMove((x,y),(x-1,y))
                    break 
                elif(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x2][y4]):
                    print('found 4 move at',x,y,'moving left around')
                    makeMove((x,y),(x-1,y))
                    break 
            #move right
            #check up
            if y>3:
                x1 = x+1
                y1 = y-1
                x2 = x+1
                y2 = y-2
                y3 = y-3
                if(y4 >= 0 and x1 <= 7):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x2][y3]):
                        print('found 4 move at',x,y,'moving right up')
                        makeMove((x,y),(x+1,y))
                        break
            #check right
            if x<4:
                x1 = x+2
                x2 = x+3
                y1 = y
                y2 = y
                x3 = x+4
                if(x4 <= 7):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x3][y2]):
                        print('found 4 move at',x,y,'moving right right')
                        makeMove((x,y),(x+1,y))
                        break
            #check down
            if y<4:
                x1 = x+1
                x2 = x+1
                y1 = y+1
                y2 = y+2
                y3 = y+3
                if(x2 <= 7 and y4 <= 7):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x2][y3] ):
                        print('found 4 move at',x,y,'moving right down')
                        makeMove((x,y),(x+1,y))
                        break
            #check around
            x1 = x+1
            x2 = x+1
            y1 = y+1
            y2 = y-1
            y3 = y+2
            y4 = y-2
            if(x2 <= 7 and y3 <= 7 and y4 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x2][y3] ):
                    print('found 4 move at',x,y,'moving right around')
                    makeMove((x,y),(x+1,y))
                    break
                elif(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x2][y4]):
                    print('found 4 move at',x,y,'moving right around')
                    makeMove((x,y),(x+1,y))
                    break
            #move down
            #check down
            x1 = x
            y1 = y+2
            x2 = x
            y2 = y+3
            y3 = y+4
            if(y3 <= 7):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x2][y3]):
                    print('found 4 move at',x,y,'moving up up')
                    makeMove((x,y),(x,y+1))
                    break
            #check left
            if x>3:
                x1 = x-1
                x2 = x-2
                y1 = y+1
                y2 = y+1
                x3 = x-3
                if(x4 >= 0 and y2 <=7):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x3][y2] ):
                        print('found 4 move at',x,y,'moving up left')
                        makeMove((x,y),(x,y+1))
                        break
            #check right
            if x <4:
                x1 = x+1
                x2 = x+2
                y1 = y+1
                y2 = y+1
                x3 = x+3
                if(x4 <= 7 and y2 <= 7):
                    if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]  == Rows[x3][y2] ):
                        print('found 4 move at',x,y,'moving up right')
                        makeMove((x,y),(x,y+1))
                        break
            #check around
            x1 = x+1
            x2 = x-1
            y1 = y+1
            y2 = y+1
            x3 = x+2
            x4 = x-2
            if(x3 <= 7 and 42 >= 0 and y2 <= 7):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x3][y2] ):
                    print('found move at',x,y,'moving up around')
                    makeMove((x,y),(x,y+1))
                    break
                elif(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2] == Rows[x4][y2]):
                    print('found move at',x,y,'moving up around')
                    makeMove((x,y),(x,y+1))
                    break
"""
#def SearchFutureFiveLShape():
#def SearchFutureFourInARow():
"""
def searchForAThree(Rows):
    for x in range(8):
        for y in range(8):
            #move up
            #check up
            x1 = x
            y1 = y-2
            x2 = x
            y2 = y-3
            if(y2 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving up up')
                    makeMove((x,y),(x,y-1))
                    break
            #check left
            x1 = x-1
            x2 = x-2
            y1 = y-1
            y2 = y-1
            if(x2 >= 0 and y2 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving up left')
                    makeMove((x,y),(x,y-1))
                    break
            #check right
            x1 = x+1
            x2 = x+2
            y1 = y-1
            y2 = y-1
            if(x2 <= 7 and y2 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving up right')
                    makeMove((x,y),(x,y-1))
                    break
            #check around
            x1 = x+1
            x2 = x-1
            y1 = y-1
            y2 = y-1
            if(x1 <= 7 and x2 >= 0 and y2 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving up around')
                    makeMove((x,y),(x,y-1))
                    break
            #move left
            #check up
            x1 = x-1
            y1 = y-1
            x2 = x-1
            y2 = y-2
            if(y2 >= 0 and x1 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving left up')
                    makeMove((x,y),(x-1,y))
                    break
            #check left
            x1 = x-2
            x2 = x-3
            y1 = y
            y2 = y
            if(x2 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving left left')
                    makeMove((x,y),(x-1,y))
                    break
            #check down
            x1 = x-1
            x2 = x-1
            y1 = y+1
            y2 = y+2
            if(x2 >= 0 and y2 <= 7):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving left down')
                    makeMove((x,y),(x-1,y))
                    break 
            #check around
            x1 = x-1
            x2 = x-1
            y1 = y+1
            y2 = y-1
            if(x2 >= 0 and y1 <= 7 and y2 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving left around')
                    makeMove((x,y),(x-1,y))
                    break 
            #move right
            #check up
            x1 = x+1
            y1 = y-1
            x2 = x+1
            y2 = y-2
            if(y2 >= 0 and x1 <= 7):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving right up')
                    makeMove((x,y),(x+1,y))
                    break
            #check right
            x1 = x+2
            x2 = x+3
            y1 = y
            y2 = y
            if(x2 <= 7):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving right right')
                    makeMove((x,y),(x+1,y))
                    break
            #check down
            x1 = x+1
            x2 = x+1
            y1 = y+1
            y2 = y+2
            if(x2 <= 7 and y2 <= 7):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving right down')
                    makeMove((x,y),(x+1,y))
                    break
            #check around
            x1 = x+1
            x2 = x+1
            y1 = y+1
            y2 = y-1
            if(x2 <= 7 and y1 <= 7 and y2 >= 0):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving right around')
                    makeMove((x,y),(x+1,y))
                    break
            #move down
            #check down
            x1 = x
            y1 = y+2
            x2 = x
            y2 = y+3
            if(y2 <= 7):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving up up')
                    makeMove((x,y),(x,y+1))
                    break
            #check left
            x1 = x-1
            x2 = x-2
            y1 = y+1
            y2 = y+1
            if(x2 >= 0 and y2 <=7):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving up left')
                    makeMove((x,y),(x,y+1))
                    break
            #check right
            x1 = x+1
            x2 = x+2
            y1 = y+1
            y2 = y+1
            if(x2 <= 7 and y2 <= 7):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving up right')
                    makeMove((x,y),(x,y+1))
                    break
            #check around
            x1 = x+1
            x2 = x-1
            y1 = y+1
            y2 = y+1
            if(x1 <= 7 and x2 >= 0 and y2 <= 7):
                if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
                    print('found move at',x,y,'moving up around')
                    makeMove((x,y),(x,y+1))
                    break