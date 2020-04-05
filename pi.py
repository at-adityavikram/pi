#import math
dx=4
i=1
while True:#  dx != math.pi:
    # the commented check was there to stop the program when dx=pi
    dx = dx*((((2*i)+1)**2)-1)/(((2*i)+1)**2)
    i+=1
    print(str(dx),end="\r")
