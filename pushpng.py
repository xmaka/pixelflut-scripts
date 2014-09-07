import Image
import sys
import random
import time

i = Image.open(sys.argv[1])
pix = i.load()

n = 45000
p = 15485867
xo = 0
yo = 0
lasttime = 0
while True:
    t = int(time.time())
    if int(t/120) != int(lasttime/120):
        lasttime = t
        random.seed(int(t/120))
        xo = random.randint(0,800-i.size[0])
        yo = random.randint(0,576-i.size[1])
        print xo, yo
    n = (n+p)%(i.size[0]*i.size[1])
    x = n % i.size[0]
    y = int  (n / i.size[0])
    if pix[x,y] == (0,0,0):
        continue
    print "px %d %d %02x%02x%02x"%(x+xo,y+yo,pix[x,y][0],pix[x,y][1],pix[x,y][2])
