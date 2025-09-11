import os
from PIL import Image, ImageOps
import random
import math




class Canvas():

    def __init__(self,canvas:Image):
        self.img = canvas


    def EINKFlip(self):
        image = self.img
        image = image.rotate(-90, expand=True)   
        image = image.transpose(Image.FLIP_TOP_BOTTOM)  
        self.img =  image
        return self.GetCanvas()
        
        

    def BWInvert(self):
        image = self.img
        image = image.convert('1')
        #newimg = ImageOps.invert(image) - bad inversion

        oldpixels = image.load()
        width, height = image.size
        newimg = Image.new('1', (width,height), color = (0))
        newpixels = newimg.load()
        for x in range(width):
            for y in range(height):
                if oldpixels[x, y]==0:
                    newpixels[x,y] = 1

        self.img =  newimg
        return self.GetCanvas()  


    def GetCanvas(self):
        return self.img   









class Sprites(Canvas):

    DISABLED = -999999

    Black = 0
    White = 1

    BLACK=0
    WHITE=1
    RED  =2
    TRANS=3

    PLASSPRITE = 10
    MINUSSPRITE = 11
    
    EXT = ".png"
    
    DIGITPLAS = 10
    DIGITMINUS = 11
    DIGITSEMICOLON = 12    
    
    CLOUDWMAX =32
    CLOUDS = [2,3,5,10,30,50]
    CLOUDK = 0.5    
    
    HEAVYRAIN = 5.0
    RAINFACTOR = 20
    
    HEAVYSNOW = 5.0
    SNOWFACTOR = 10    
    
    
    SMOKE_R_PX = 30
    PERSENT_DELTA = 4
    SMOKE_SIZE = 60
    
    

    def __init__(self,spritesdir:str,canvas:Image):
        super().__init__(canvas)
        self.pix = self.img.load()
        self.dir = spritesdir
        self.ext = self.EXT
        self.w, self.h = canvas.size


    def Dot(self,x,y,color):
    
        #y = self.h - y
    
        if (y>=self.h) or (x>=self.w) or (y<0) or (x<0):
            return
    
        self.pix[x,y] = color
        


    def GetSprite(self,name,index)->Image:
        imagefilename = "%s_%02i%s" % (name, index, self.ext)
        imagepath = os.path.join(self.dir,imagefilename) 
        img = Image.open(imagepath)
        return img


    def Draw(self,name,index,xpos,ypos,ismirror=False):

        if (xpos<0) or (ypos<0):
            return 0

        #print("DRAW '%s' #%i at %i,%i" % (name,index,xpos,ypos))
    
        img = self.GetSprite(name,index)
        if (ismirror):
            img = ImageOps.mirror(img)
        w, h = img.size
        pix = img.load()
        ypos -= h
        for x in range(w):
            for y in range(h):
                if (xpos+x>=self.w) or (xpos+x<0):
                    continue
                if (ypos+y>=self.h) or (ypos+y<0):
                    continue
               
                if (pix[x,y]==self.BLACK):
                    self.Dot(xpos+x,ypos+y,self.Black)
                elif (pix[x,y]==self.WHITE):
                    self.Dot(xpos+x,ypos+y,self.White)
                elif (pix[x,y]==self.RED):
                    self.Dot(xpos+x,ypos+y,self.Black)

        return w



    def DrawDigit(self,id,xpos,ypos):
        return self.Draw("digit",id,xpos,ypos)
    


    def DrawInt(self,n,xpos,ypos,issign=True,mindigits=1):
        n = round(n)
        if (n<0):
            sign = self.DIGITMINUS
        else:
            sign = self.DIGITPLAS
        n = round(n)
        n = abs(n)
        n0 = int( n / 100 )
        n1 = int( (n % 100) / 10 )
        n2 = n % 10
        dx = 0
        if (issign) or (sign == self.DIGITMINUS):
            w = self.DrawDigit(sign,xpos+dx,ypos)
            dx+=w+1
        if (n0!=0) or (mindigits>=3):
            w = self.DrawDigit(n0,xpos+dx,ypos)
            dx+=w
            if (n0!=1):
                dx+=1
        if (n1!=0) or (n0!=0)  or (mindigits>=2):
            if (n1==1):
                dx -=1
            w = self.DrawDigit(n1,xpos+dx,ypos)
            dx+=w
            if (n1!=1):
                dx+=1
        if (n2==1):
            dx -=1                
        w = self.DrawDigit(n2,xpos+dx,ypos)
        dx+=w
        if (n2!=1):
            dx +=1                
        return dx
        
        
        
        

    def DrawClock(self,xpos,ypos,h,m):
        dx=0
        w = self.DrawInt(h,xpos+dx,ypos,False,2)
        dx+=w
        w = self.DrawDigit(self.DIGITSEMICOLON,xpos+dx,ypos)
        dx+=w
        dx = self.DrawInt(m,xpos+dx,ypos,False,2)
        dx+=w+1
        return dx






    def DrawCloud(self,persent,xpos,ypos,width,height):
        if (persent<2):
            return
        elif (persent<5):
            cloudset = [2]
        elif (persent<10):
            cloudset = [3,2]
        elif (persent<20):
            cloudset = [5,3,2]
        elif (persent<30):
            cloudset = [10,5]
        elif (persent<40):
            cloudset = [10,10]
        elif (persent<50):
            cloudset = [10,10,5]
        elif (persent<60):
            cloudset = [30,5]
        elif (persent<70):
            cloudset = [30,10]
        elif (persent<80):
            cloudset = [30,10,5,5]
        elif (persent<90):
            cloudset = [30,10,10]
        else:
            cloudset = [50,30,10,10,5]

        dx = width 
        dy = 16
        for c in cloudset: 
            self.Draw("cloud",c,xpos+random.randrange(dx),ypos)
        


    def DrawRain(self,value,xpos,ypos,width,tline,dotcolor=None):
        ypos+=1
        r = 1.0 - ( value / self.HEAVYRAIN ) / self.RAINFACTOR 

        for x in range(xpos,xpos+width):
            
            for y in range(ypos,tline[x],2):
                if (x>=self.w): 
                    continue
                if (y>=self.h): 
                    continue
                if (random.random()>r):
                    self.pix[x,y] = self.Black if dotcolor==None else dotcolor
                    self.pix[x,y-1] = self.Black if dotcolor==None else dotcolor
        

    
    def DrawSnow(self,value,xpos,ypos,width,tline,dotcolor=None):
        ypos+=1
        r = 1.0 - ( value / self.HEAVYSNOW ) / self.SNOWFACTOR 

        for x in range(xpos,xpos+width):
            for y in range(ypos,tline[x],2):
                if (x>=self.w): 
                    continue
                if (y>=self.h): 
                    continue
                if (random.random()>r):
                    self.pix[x,y] = self.Black if dotcolor==None else dotcolor


    def DrawSoil(self,tline:list[int],xoffset =0, dotcolor=None):
        width = len(tline)
        for x in range(width):
            self.Dot(x+xoffset,tline[x],self.BLACK if dotcolor==None else dotcolor)



    def  DrawWind_degdist(self, deg1,deg2 ):
        h = max(deg1,deg2)
        l = min(deg1,deg2)
        d = h-l
        if (d>180):
            d = 360-d
        return d
    


    def DrawWind_dirsprite(self,dir,dir0,name,list):
        count = [4,3,3,2,2,1,1]
        step = 11.25 #degrees
        dist = self. DrawWind_degdist(dir,dir0)
        n = int(dist/step)
        if (n<len(count)):
            for i in range(0,count[n]):
                list.append(name)
        




    def DrawWind(self,speed,direction,xpos,tline):
            
        list = []

        self.DrawWind_dirsprite(direction,0,  "pine",list)
        self.DrawWind_dirsprite(direction,90, "east",list)
        self.DrawWind_dirsprite(direction,180,"palm",list)
        self.DrawWind_dirsprite(direction,270,"tree",list)

        random.shuffle(list)

        windindex = None
        if   (speed<=0.4):
            windindex = []
        elif (speed<=0.7):
            windindex = [0]
        elif (speed<=1.7):
            windindex = [1,0,0]
        elif (speed<=3.3):
            windindex = [1,1,0,0]
        elif (speed<=5.2):
            windindex = [1,2,0,0]
        elif (speed<=7.4):
            windindex = [1,2,2,0]
        elif (speed<=9.8):
            windindex = [1,2,3,0]
        elif (speed<=12.4):
            windindex = [2,2,3,0]            
        else:
            windindex = [3,3,3,3]    
        
        if (windindex!=None):
            ix = int(xpos)
            random.shuffle(windindex)
            j=0
            #print("wind>>>",direction,speed,list,windindex);
            for i in windindex:

                xx  = ix + random.randint(-1, 1)
                ismirror = random.random() < 0.5
                offset = xx+5

                if (offset>=len(tline)):
                    break
                
                if (ismirror):
                    xx -= 16

                self.Draw(list[j],i,xx,tline[offset]+1,ismirror) 
                ix+=9
                j+=1
            



   

    def DrawSmoke_makeline(self,angle_deg):
        a = (math.pi  * angle_deg) / 180
        r = self.SMOKE_R_PX
        k = r * math.sin(a) / ( math.sqrt( ( r * math.cos(a) )) ) 
        yp = 0
        dots=[]
        for x in range(0,self.w):
            y = int( k * math.sqrt(x) )
            if (y>self.h):
                y = self.h
            yi = yp
            while(True):
                rr = math.sqrt( x*x + yi*yi )
                dots.append( [x,yi,rr] )
                if (rr>self.SMOKE_SIZE):
                    return dots
                yi+=1
                if (yi>=y):
                    yp = y
                    break

    
    
    def MakeSmokeAt(self,x,y,index:int):
        self.Dot(x, y, self.Black )
        

    def DrawSmoke(self,x0,y0,persent):
        dots = self.DrawSmoke_makeline(persent)
        i=0
        for d in dots:
            x = d[0]
            y = d[1]
            r = d[2]
            
            if random.random()*1.3 > (r/self.SMOKE_SIZE):
                if random.random()*1.2 < (r/self.SMOKE_SIZE):
                    dx = random.randint(-1, 1)
                    dy = random.randint(-1, 1)
                else:
                    dx = 0
                    dy = 0
                self.MakeSmokeAt(x0+x+dx, self.h-(y0+y)+dy,i)
                
            i+=1


        
    
    




if __name__ == "__main__":  


    img = Image.open('../test.bmp')
    
    
    s = Sprites('../sprite',img)
    
    
    s.Draw("house",0,100,100)
    
    img.save("../tmp/sprites_test.bmp")
    
    