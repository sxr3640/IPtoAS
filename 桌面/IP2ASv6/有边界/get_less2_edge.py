import sys
f2=open("get_Dict_edge","r")
f3=open("result_edge_less2_tmp1.txt","w")
for k in f2:
    tmp1=k.split(':')
    l=0
    val=tmp1[1].split(',')
    #print tmp1[0]
    while 1:
        try:
            if int(val[l][0])>2:
                break
            else:
                l=l+1
        except:
            f3.write(k)
            #print k
            break
f2.close()
f3.close()
f = open("result_edge_less2_tmp1.txt","r")
f1 =open("result_edge_less2_tmp2.txt","a")
for i in f:
    print i
    i=i.rstrip('\n')
    i=i.rstrip()
    tmp = i.split(':')
    f1.write(tmp[0]+":")
    tmp1 = tmp[1].split(',')
    tmp1.sort()
    myset = set(tmp1)
    for item in myset:
        f1.write(item+"("+str(tmp1.count(item))+")"+'  ')
    f1.write('\n')
f.close()
f1.close()
f4=open("result_edge_less2.txt","a")
f5=open("result_edge_less2_tmp2.txt","r")
D={}
k=0
m=0
n=0
for j in f5:
    tmp2=j.split(':')
    if tmp2[0].find("_")!=-1:
        f4.write(j)
    elif tmp2[0].find(";")!=-1:
	f4.write(j)
    elif tmp2[0]=="None":
	    f4.write(j)
    elif tmp2[0]=="q":
	    f4.write(j)
    else:
        try:
            D[int(tmp2[0])]=tmp2[1]
            k=k+1
        except:
            break
#L.sort(key=operator.itemgetter(0))
sorted(D.keys())
for m in sorted(D.keys()):
    f4.write( str(m)+':'+D[m])

