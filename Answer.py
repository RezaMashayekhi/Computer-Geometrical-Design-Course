import math
import random


class point:
  a=0.0
  i=0
  def __init__(self,x,y):
    self.x=x
    self.y=y



def angle(v1, v2):        #zavie v1 nesbat be v2 dar jahat pad saatgard
    x1= v1.x
    y1=v1.y
    x2 = v2.x
    y2 = v2.y
    inner_product = x1*x2 + y1*y2
    len=math.sqrt(((x1*x1)+(y1*y1)) * ((x2*x2)+(y2*y2)))

    #chap ya rast boodan v1 nesbat be v2

    xp = x1 * y2 - y1 * x2  # Cross product
    if xp > 0:       #v1 samte raste v2 ast
      return (2*math.pi)-math.acos(inner_product / len)
    else:            #v1 samte chape v2 ast
      return math.acos(inner_product/len)

def comp(p1,p2):        #p1 ghable p2 hast ya na
    if(( (p1.x>=0 and p2.x>=0 and p1.y>=0 and p2.y>=0) or (p1.x<0 and p2.x<0 and p1.y>=0 and p2.y>=0) or (p1.x<0 and p2.x<0 and p1.y<0 and p2.y<0)or (p1.x>=0 and p2.x>=0 and p1.y<0 and p2.y<0)) and p1.x*p2.y==p1.y*p2.x):
        if (p1.x * p1.x + p1.y * p1.y < p2.x * p2.x + p2.y * p2.y):
            return 1
        else:
            return 0
    if(p1.a<p2.a):
        return 1
    if(p1.a>p2.a):
        return 0
    #if(p1.x*p1.x+p1.y*p1.y<p2.x*p2.x+p2.y*p2.y):
    #    return 1
    return 0

def ran():          #yek adad beine -100 ta 100
    x=random.randint(0,1)
    if(x==1):
        return random.random() * 100
    else:
        return -1*(random.random() * 100)


a=[]
v2=point(1,0)

p0=point(ran(),ran())
p=point(0,0);
a.append(p)
print(str(p0.x)+" "+str(p0.y))
p1=point(ran()-p0.x,ran()-p0.y)
p1.a=angle(p1,v2)
p1.i=1
a.append(p1)
print(str(p1.x)+" "+str(p1.y))
p2=point(ran()-p0.x,ran()-p0.y)
p2.a=angle(p2,v2)
p2.i=2
print(str(p2.x)+" "+str(p2.y))
if(comp(p1,p2)):
    a.append(p2)
else:
    a.insert(1,p2)


c=3
g=random.randint(0,10000) # haman tedad noghat
i=0
while i<g:
    p = point(ran() - p0.x,ran() - p0.y)
    print(str(p.x)+" "+str(p.y))
    p.a = angle(p, v2)
    p.i=c
    f=0
    for i in range(1,len(a)):
        if(comp(a[i-1],p) and comp(p,a[i])):
            a.insert(i,p)
            f=1

    if(f==0):
        a.append(p)
    c=c+1
    i=i+1

#print(angle(p,v2)*360/(2*math.pi))
print("end*******************")
for i in a:
    print(i.i)