"""input
5
"""
import math

Data=[]
F=open("input.txt","r")
st=F.readline().strip()
while st:
	Data.append(st.split(","))
	st=F.readline().strip()

Class=5
Class-=1
Classes=["Outlook","Temp.","Humidity","Wind","Play Tennis"]
def entropy(Data,class_to_divide):
	Mset=set()
	Class=len(Data[0])-1
	for i in range(len(Data)):
		Mset.add(Data[i][Class])
	Mset=list(Mset)
	cset=set()
	for i in range(len(Data)):
		cset.add(Data[i][class_to_divide])
	cset=list(cset)
	num=[]
	for i in range(len(cset)):
		num.append([0]*len(Mset))
	
	for i in range(len(Data)):
		num[cset.index(Data[i][class_to_divide])][Mset.index(Data[i][Class])]+=1
	entropy=0
	
	for i in range(len(cset)) :
		for j in range(len(Mset)):
			if num[i][j]>0:
				entropy+=((num[i][j]/float(sum(num[i])))*math.log((num[i][j]/float(sum(num[i])))))/math.log(2)
		entropy*=float(sum(num[i]))/float(len(Data))
	print num,entropy
	return entropy

def decompose(Data,Classes):
	Mset=set()
	Class=len(Data[0])-1
	for i in range(len(Data)):
		Mset.add(Data[i][Class])
	Mset=list(Mset)

	E=[-999999]*len(Data[0])
	for i in range(len(Data[0])):
		if i!=Class:
			E[i]=entropy(Data,i)

	div=E.index(max(E))
	print E,Classes
	cset=set()
	for i in range(len(Data)):
		cset.add(Data[i][div])
	cset=list(cset)
	if E[div]==0:
		
		return 
	NewD=[]
	print Classes[div]
	for i in range(len(cset)):
		NewD.append([])
	for i in range(len(Data)):
		ND=Data[i][:]
		ND.pop(div)
		NewD[cset.index(Data[i][div])].append(ND)
	C=Classes[:]
	C.pop(div)
	for i in NewD:
		decompose(i,C)
decompose(Data,Classes)
	

