import numpy as np
import scipy
import random
import math
import matplotlib as ml
import matplotlib.pyplot as plt
#parameters
L=20
T=10000
temp=1
J=1
H=0
fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)
plt.ion()
plt.show()
config=np.zeros(shape=(L,L))
prob=np.zeros(shape=9)
#initialization.
for i in range (0,L):
	for j in range (0,L):
		s=np.random.uniform(0,1)
		if s>0.5:
			config[i][j]=1
		else:
			config[i][j]=-1
def cal_mag():
	mag=np.sum(config)
	return mag/(L*L)
def PR(temp):
	for m in range (-4,5):
		Ep=-J*m-H
		Em=J*m+H
		prob[m+4]=math.exp(-Ep*(1.0/temp))/(math.exp(-Ep*(1.0/temp))+math.exp(-Em*(1.0/temp)))
		#print prob[m+4],m

def nei(x,y):
	m=0
        if x==L-1:
                m=m+config[0][y]
        else:
                m=m+config[x+1][y]
        if x==0:
                m=m+config[L-1][y]
        else:
                m=m+config[x-1][y]
        if y==L-1:
                m=m+config[x][0]
        else:
                m=m+config[x][y+1]
        if y==0:
                m=m+config[x][L-1]
        else:
                m=m+config[x][y-1]
        return m

def mcmove(temp):
	x=np.random.randint(0,L)
	y=np.random.randint(0,L)
	m=nei(x,y)
	s=np.random.uniform(0,1)
	#print prob[m+4],s
	if s>prob[m+4]:
		config[x][y]=-1
	else :
		config[x][y]=1
temp=5
while 1:
	plt.imshow(config)
	ax.set_title( plt.title('temp=%f'%temp) )
	ax.set_aspect('equal')
	plt.draw()
	M1=0
	if temp<.01:
		break
	PR(temp)
	for i in range (0,T):
		mcmove(temp)
		M=cal_mag()
	#	print i,abs(M)
	for i in range (0,T):
		mcmove(temp)
		mag=cal_mag()
		M1=M1+mag
	print temp,abs(M1/T)
	temp=temp-.1
#	break	
