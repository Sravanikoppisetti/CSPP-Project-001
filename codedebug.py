EMPTY_UNCLICKED = 1
def emptygrid(rows,col):
    grid=[]
    for i in range(rows):
        x=[]
        for j in range(col):
            x.append(EMPTY_UNCLICKED )
        grid.append(x)
    return grid
print(emptygrid(5,6))
