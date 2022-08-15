# def drawLine( length, direction ):

# drawLine( 5, 'h' )
#   -----
# drawLine( 5, 'v' )
# |
# |
# |
lengt = 5
directions = input( "Enter the directions 'h' or 'v': ")
def drawLine (lengt, directions):
    if directions == 'h' and lengt == 5:
        print("-"*5)
    elif directions == "v":
        for i in range(4,1,-1):
            print("|")
        
drawLine(5,'h')
drawLine(5,'v')