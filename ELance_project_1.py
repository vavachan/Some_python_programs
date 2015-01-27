import math
import random
import numpy as np
from scipy.optimize import fmin
def fcn(x,y):
	z=math.exp(math.sin(50.0*x))+math.sin(60.0*math.exp(y))+math.sin(80.0*math.sin(x))+math.sin(math.sin(70.0*y))-math.sin(10.0*(x+y))+(x*x+y*y)/4.0
	return z
def fcn1(x):
	z=math.exp(math.sin(50.0*x[0]))+math.sin(60.0*math.exp(x[1]))+math.sin(80.0*math.sin(x[0]))+math.sin(math.sin(70.0*x[1]))-math.sin(10.0*(x[0]+x[1]))+(x[0]*x[0]+x[1]*x[1])/4.0
	return z


dx=.001
dy=.001
i=0
x=np.zeros(2)
N=10000 #The number of random search starting points.
data=np.zeros((3,N+1))
best=5
bestx=0
besty=0
while 1:	
	x[0]=random.uniform(-1,1)# Random starting point initilization
	x[1]=random.uniform(-1,1)# "
	zb=fcn(x[0],x[1])
	xb=x[0]
	yb=x[1]
	while 1:
		p=0
		x[0]=xb
		x[1]=yb
		z=zb
		if x[0]-dx<-1:#Applying the limits of search domain.
			x[0]=-1
		if x[0]+dx>1:
			x[0]=1
		if x[1]-dy <-1:
			x[1]=-1
		if x[1]+dy >1:
			x[1]=1
		zxp=fcn(x[0]+dx,x[1])
		zyp=fcn(x[0],x[1]+dy)
		zxm=fcn(x[0]-dx,x[1])
		zym=fcn(x[0],x[1]-dy)
		if zxm<zb:
			zb=zxm	
			xb=x[0]-dx
		if zxp<zb:
			zb=zxp
			xb=x[0]+dx
		if zxm<z and z<zxp:
			dx=2*dx
		if zxm<z and zxp<z:
			dx=dx/2	
		if z<zxp and z<zxm: 
			dx=dx/2
		if zxm>z and zxp<z:
			dx=2*dx
		########################################################
		if zym<zb:
			zb=zym	
			yb=x[1]-dy
		if zyp<zb:
			zb=zyp
			yb=x[1]+dy
		if zym<z and z<zyp:
			dy=2*dy
		if zym<z and zyp<z:
			dy=dy/2	
		if z<zyp and z<zym: 
			dy=dy/2
		if zym>z and zyp<z:
			dy=2*dy
		p=p+1
		if zb==z:
			break
	if best>fcn(xb,yb):
		best=fcn(xb,yb)	
		bestx=xb
		besty=yb
	i=i+1
	if i>N:
		break
x[0]=bestx
x[1]=besty
mi=fmin(fcn1,x)#To further converge to the point.
if mi[0]>1:
	mi[0]=1
if mi[0]<-1:
	mi[0]=-1
if mi[1]>1:
	mi[1]=1
if mi[1]<-1:
	mi[1]=-1
print mi,fcn1(mi)
