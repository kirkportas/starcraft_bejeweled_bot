import sys
from PyQt4 import QtGui, QtCore
import autopy
import math
from PIL import Image, ImageStat, ImageGrab
import time
from findmove import *
#import getscreen

# Game board
Column1 = [0,0,0,0,0,0,0,0] 
Column2 = [0,0,0,0,0,0,0,0] 
Column3 = [0,0,0,0,0,0,0,0] 
Column4 = [0,0,0,0,0,0,0,0] 
Column5 = [0,0,0,0,0,0,0,0] 
Column6 = [0,0,0,0,0,0,0,0] 
Column7 = [0,0,0,0,0,0,0,0] 
Column8 = [0,0,0,0,0,0,0,0] 
Rows = [Column1,Column2,Column3,Column4,Column5,Column6,Column7,Column8]
C1 = [0,0,0,0,0,0,0,0] 
C2 = [0,0,0,0,0,0,0,0] 
C3 = [0,0,0,0,0,0,0,0] 
C4 = [0,0,0,0,0,0,0,0] 
C5 = [0,0,0,0,0,0,0,0] 
C6 = [0,0,0,0,0,0,0,0] 
C7 = [0,0,0,0,0,0,0,0] 
C8 = [0,0,0,0,0,0,0,0] 
R = [C1,C2,C3,C4,C5,C6,C7,C8]

moveCounter = 0
gameOverCounter = 0

# rgb values for the screenshots of individual pieces. Calced with py rgb tools, averages found in excel.
rgbdict = {
           'blue':[70.48478993, 141.0030965, 171.4636593],  #1
           'red':[115.3613444,45.95710092, 26.07481793],   #2
           'yellow':[112.6464526,111.6639913,52.30208746], #3
           'black':[73.57383609,71.45632489, 68.75964968],  #4
           'purple':[72.05809411,38.0068371,77.13559538], #5
           'green':[73.43107695,132.0023781,41.93863598] #6                   
           }

                   
#Top left corner of game square
xref, yref = 940, 105   #Pixel values on monitor
global sqw, sqh, x1, y1
sqw = 58  #58.375 in windowed on 1440x900 monitor
sqh = 58
#Middle of first square
x1 = xref + 29
y1 = yref + 29
        

# for lists in dict
#avar = thisdict["secondval"]
#avar[0]

def main():
    while True:
        t0 = time.time()
        
        while ((time.time()-t0) < 10 ): # limits time bot is run
            print('mainloopcounter')
            print('getscreen')
            getScreen()
            print('Finding Move')
            findMove(Rows)
            print('found no moves')
            print(Column1)
            print(Column2)
            print(Column3)
            print(Column4)
            print(Column5)
            print(Column6)
            print(Column7)
            print(Column8)
        raw_input("press enter")
    print 'ended'
            

def captureScreenshot():
    sender = sender()
    statusBar().showMessage(sender.text() + ' was pressed')
    
    for y in reversed(range(8)):
        for x in reversed(range(8)):
            R[x][y] = autopy.screen.get_color((400+(x*40)),(480+(y*40)))
            print R[x][y]

def getScreen():
    # Grab image and crop it to the desired window
    box = (940, 105, 1407, 572)
    im = ImageGrab.grab().crop(box)
    #im.save('testcrop.jpg')
    
    #Iterate through each piece in reverse, on xy scale
    for y in reversed(range(8)):
        for x in reversed(range(8)):
            #sqh,sqw are height and width of game piece squares
            #each pieceim is a square holding the game piece
            piecebox = ( sqw*(x), sqh*(y), sqw*(x+1), sqh*(y+1))
            pieceim = im.crop(piecebox)
            #pieceim.save('piececrop_xy_'+ str(x) + str(y) + '.jpg')
            
            stats = ImageStat.Stat(pieceim)
            statsmean = stats.mean
            #update array with game state of each piece.
            Rows[x][y] = whichpiece(statsmean)
            


def whichpiece(statsmean):
    bestScore = 255
    curScore= 0
    pieceColor = 'empty'
    for key in rgbdict.keys():
        curScore = (math.pow( (statsmean[0]/255) - (rgbdict[key][0]/255), 2)
            +  math.pow( (statsmean[1]/255) - (rgbdict[key][1]/255), 2)
            +  math.pow( (statsmean[2]/255) - (rgbdict[key][2]/255), 2) )
        if curScore < bestScore:
            pieceColor = key
            bestScore = curScore       
            
    
    if bestScore > 1:
        sys.exit
    rgbdictnumb = {'blue':1,  #1
               'red':2,   #2
               'yellow':3, #3
               'black':4,  #4
               'purple':5, #5
               'green':6, #6
               'empty':0
               }
    return rgbdictnumb[pieceColor]
    
def delay(length):
    for x in range(length):
        for y in range(length):
            pass

def makeMove(fromLoc, toLoc):
    print(moveCounter,'from',fromLoc,'to',toLoc)
    autopy.mouse.move((fromLoc[0]*sqw)+x1,(fromLoc[1]*sqh)+y1)
    #mouse.move here above
    #delay(250)
    delay(2300)
    autopy.mouse.click(True)
    #autopy.mouse.toggle(True)
    #delay(250) # too fast.
    delay(2300) # Assumes prior click was successful. (85%+ it is)
    try:
        # use smooth_move to emulate human mouse movement, less obviously a bot
        autopy.mouse.smooth_move(((toLoc[0]*sqw)+x1),((toLoc[1]*sqh)+y1)) 
        autopy.mouse.click(True)
    except ValueError:
        #print('valueerror ',((toLoc[0]*40)+400),((toLoc[1]*40)+480))
        #delay(200000)
        autopy.mouse.toggle(False)
        return
    #delay(200)
    delay(1500)
    autopy.mouse.toggle(False)


if __name__ == '__main__':
    main()
    