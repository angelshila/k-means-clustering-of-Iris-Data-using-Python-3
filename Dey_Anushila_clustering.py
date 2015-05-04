import sys
from operator import itemgetter

"Opening input file"
file_name = sys.argv[1]
clustersize= int(sys.argv[2])
iterations = int(sys.argv[3])
initial_points = sys.argv[4]

"Reading input file"
doc = open(file_name).read()

"Removing Newline Characters"
newfile=doc.splitlines()

"Reading initial points"
doc1= open(initial_points).read()
newfile2=doc1.splitlines()

"Making List for input file"
newlist=[]
for x in newfile:
	newlist.append(x.split(','))

"Making List of Lists for initial_points"
newlist3=[]
for x in newfile2:
    newlist3.append(x.split(','))

"Make new dictionary of clusters"
group={}
for i in newlist3:
    group[','.join(i)]=[]

"Assign Points to clusters"
mincluster=[]
mindistpt=10 ** 10
for x in newlist:
    for key in group:
        dist= ((float(x[0])-float(key.split(',')[0])) ** 2 + (float(x[1])-float(key.split(',')[1])) ** 2 + (float(x[2])-float(key.split(',')[2])) ** 2 + (float(x[3])-float(key.split(',')[3])) ** 2) ** 0.5
        if dist!=0.0 and mindistpt > dist:
            mindistpt = dist
            mincluster=key.split(',')
    group[','.join(mincluster)].append(x)
    mindistpt=10**10

# for key,value in group.items():
#     print(key)
#     for value in group[key]:
#         print(value)

"Number of Iterations"
k=1
while k<iterations:
    trycentroid=[]
    for key in group:
        firstquad=0.0
        secquad=0.0
        thirdquad=0.0
        fourthquad=0.0
        versicolor=0
        setosa=0
        virginica=0
        for j in group[key]:
            if j[4]=="Iris-versicolor":
                versicolor+=1
            elif j[4] == "Iris-setosa":
                setosa+=1
            else:
                virginica+=1
            firstquad+=float(j[0])
            secquad+=float(j[1])
            thirdquad+=float(j[2])
            fourthquad+=float(j[3])
        firstquad=firstquad/(len(group[key]))
        secquad/=(len(group[key]))
        thirdquad/=(len(group[key]))
        fourthquad/=(len(group[key]))
        # print(setosa,versicolor,virginica)
        dict1={"Iris-setosa":setosa,"Iris-virginica":virginica,"Iris-versicolor":versicolor}
        # print(max(dict1, key=dict1.get))
        trycentroid.append([str(firstquad),str(secquad),str(thirdquad),str(fourthquad),max(dict1, key=dict1.get)])
     
    "Clear dictionary of unwanted centroids"
    group.clear()
    group={}
    for i in trycentroid:
        group[','.join(i)]=[]

    for x in newlist:
        for key in group:
            dist= ((float(x[0])-float(key.split(',')[0])) ** 2 + (float(x[1])-float(key.split(',')[1])) ** 2 + (float(x[2])-float(key.split(',')[2])) ** 2 + (float(x[3])-float(key.split(',')[3])) ** 2) ** 0.5
            if dist!=0.0 and mindistpt > dist:
                mindistpt = dist
                mincluster=key.split(',')
        group[','.join(mincluster)].append(x)
        mindistpt=10*10

    k+=1

"For printing purposes change coordinates from str to float"
for key,value in group.items():
    for i in range(0,len(group[key])):
        group[key][i]=[float(m) for m in group[key][i][:4]]+group[key][i][4:]

"Sort Dictionary in List"
finalgroup=sorted(([k,v] for k,v in group.items()))

"Printing final output"
wrongassignment=0
for f in finalgroup:
    print("cluster :",f[0].split(',')[4])
    for j in range(1,len(f)):
        for k in f[j]:
            if k[4]!=f[0].split(',')[4]:
                wrongassignment+=1
            print(k)
    print("\n")

print("Number of points wrongly assigned")
print(wrongassignment)
   


