#implementation of pcla
ps=0.5 	#desired level of coverage
pth=0.5 	#pthreshold
tk=3	#max number of cycles
w=[]	#set of nodes chosen
t=[]	#set of nodes not chosen
ew=0	#avg residual energy of nodes in w
tn=50 	#set to cardinality of nodes
en=0	#dynamic avg residual energy of nodes in w
n=0		#number of cycles of pcla