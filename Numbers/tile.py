'''
Find Cost of Tile to Cover W x H Floor – 
Calculate the total cost of tile it would take to cover a floor plan of 
width and height, using a cost entered by the user.
'''

calculate = lambda w,h,c: w * h * c

def main():
    w = int(raw_input("Please enter the width."))
    h = int(raw_input("Please enter the height."))
    c = int(raw_input("Please enter the cost per tile."))

    print calculate(w,h,c)

if __name__ == '__main__':
    main()
