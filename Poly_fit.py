import numpy as np 
#Initial Data
thrusty=[0,6,11.2,5.6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,0]
print 'Enter the Degree of the polynomial:'
k=input()
i=0
j=0
p=0
#Defining the Matrices Needed
#############################3
err=np.zeros(shape=(20))
X = np.zeros(shape=(20,k))
Xtr = np.zeros(shape=(k,20))
thrustx=np.zeros(shape=(20))
###############################
for i in range (0,20):
	thrustx[i]=i*1.0
#Initializing the Matrix(vandermode)
for i in range (0,20):
	for j in range (0,k):
		X[i,j]=pow(thrustx[i],j)
#####################################
Xtr=np.transpose(X)
####################################
XtX=np.zeros(shape=(k,k))
XtX=np.dot(Xtr,X)
####################################
A=np.zeros(shape=(k))
RHS=np.dot(Xtr,thrusty)
##################################
#Solving the Linear Equation
A=np.linalg.solve(XtX,RHS)
###################################
for i in range (0,k/2):
	swap=A[i]
	A[i]=A[k-i-1]
	A[k-i-1]=swap
#I had to reverse the order to fit with rest of the program
###################################
#Writing the Data
infile=open("Graph.dat","w")
yf = np.polyval(np.poly1d(A), thrustx)

for i in range (0,20):
	s=str(thrustx[i]/10.0)
	s1=str(yf[i])
	infile.write ('%s\t'% s)
	infile.write ('%s\n'% s1)
RMS=0
avg=0
infile2=open("coefficents.dat","a")
infile2.write('\norder:')
infile2.write(str(k))
infile2.write("\n")
infile2.write(str(A))
newfile=open("error.dat","a")
for i in range (0,20):
	err[i]=(thrusty[i]-yf[i])
	avg=avg+np.linalg.norm(err[i])
	RMS=RMS+pow((thrusty[i]-yf[i]),2)
newfile.write('Order:')
newfile.write(str(k))
newfile.write(' RMS=')
newfile.write(str(pow(RMS/20,.5))),
newfile.write(' Maximum Error:')
newfile.write(str(max(err)))
newfile.write(' Average Error:')
newfile.write(str(avg/20))
newfile.write('\n')
