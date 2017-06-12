import random
import time

class Crumbler:
    CRUMBLERS = []
    MAX = 30
    @classmethod
    def cleanup (cls):
        for c in cls.CRUMBLERS[cls.MAX:]:
            cls.CRUMBLERS.remove(c)
            del(c)

    @classmethod
    def init(cls):
        cls.CRUMBLERS=[Crumbler(500,350)]

    @classmethod
    def loop(cls):
        while True:
            for c in cls.CRUMBLERS:
                c.step()

    def __init__(self,x,y,r=None,g=None,b=None):
        self.x = x
        self.y = y
        self.a_x = random.randint(-1,1)
        self.a_y = random.randint(-1,1)
        self.steps = 0
        if r is None and g is None and b is None:
            self.r = random.randint(0,255)
            self.g = random.randint(0,255)
            self.b = random.randint(0,255)
        else:
            self.r = r
            self.g = g
            self.b = b
        if len(Crumbler.CRUMBLERS) >= Crumbler.MAX:
            Crumbler.cleanup()
        Crumbler.CRUMBLERS.append(self)
    
    def out_of_bounds(self):
        return self.x < 0 or self.y < 0 or self.x > 1920 or self.y > 1080
        
    def step(self):
        self.x += self.a_x
        self.y += self.a_y
        self.steps += 1
        if self.out_of_bounds():
            Crumbler.CRUMBLERS.remove(self)
            del(self)
            return
        print "PX %d %d %02x%02x%02x"%(self.x,self.y,self.r,self.g,self.b)
        if self.steps%7==0 or random.randint(0,5) == 3:
            x = random.randint(-20,20)
            if x%3 == 0:
                self.r += x
                self.r = min(self.r, 255)
                self.r = max(self.r, 0)
            elif x%3 == 1:
                self.g += x
                self.g = min(self.g, 255)
                self.g = max(self.g, 0)
            elif x%3 == 2:
                self.b += x
                self.b = min(self.b, 255)
                self.b = max(self.b, 0)
            self.a_x = random.randint(-1,1)
            self.a_y = random.randint(-1,1)
            if random.randint(0,2) == 2:
                Crumbler(self.x,self.y, self.r, self.g, self.b)

random.seed(time.time()**20)
Crumbler.init()
Crumbler.loop()   
