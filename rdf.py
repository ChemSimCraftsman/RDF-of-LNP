#import library

import math
import matplotlib.pyplot as plt


#creating array and taking input

one=[]
two=[]
gr=[]
r_cut=float(input("enter cutoff distance: "))
binsize=float(input("enter binsize: "))
filename=input("enter filename(with extensions): ")
atomtype1=int(input("enter atom type 1: "))
atomtype2=int(input("enter atom type 2: "))
skip=int(input("frames to skip"))

#initializong res
res=[0]*(int(r_cut/binsize)+2)
#for i in range(int(r_cut/binsize)+1):
#    res.append(0)

inf=open(filename,"r")
for i in range(3):
    inf.readline()

#no_atoms
no_atoms=int(inf.readline())
inf.readline()
inf.readline()
inf.readline()
inf.readline()

#finding indices
a=inf.readline().strip(" ").split()
inf.close()
atom_index=a.index("id")-2    
type_index=a.index("type")-2
x_index=a.index("x")-2
y_index=a.index("y")-2
z_index=a.index("z")-2


#reading atom information

f=open(filename,"r")
for i in range((no_atoms+9)*skip):
    f.readline()
nframe=1
while True:
    print("%d frame processed"%int(nframe))
    nframe+=1
    for i in range(5):                                        #skip intital 9 lines
        eof=f.readline() 
    if not eof: break                                         #checking if is it end of file 
    xlo,xhi=list(map(float,f.readline().strip().split()))     #reading box lenght in every frame
    ylo,yhi=list(map(float,f.readline().strip().split()))
    zlo,zhi=list(map(float,f.readline().strip().split()))    
    xl=xhi-xlo
    yl=yhi-ylo
    zl=zhi-zlo
    f.readline()                                              #skipping line with coloumn names
    for j in range(no_atoms):
        data=f.readline().strip().split()
        a_id,a_type,x_coor,y_coor,z_coor=int(data[atom_index]),int(data[type_index]),float(data[x_index]),float(data[y_index]),float(data[z_index])
        if a_type==atomtype1:
            one.append([a_id,x_coor,y_coor,z_coor])
        if atomtype1!=atomtype2 and a_type==atomtype2:
            two.append([a_id,x_coor,y_coor,z_coor])
    if atomtype1==atomtype2:
        two=one            
    for k in range(len(one)):
        for l in range(k+1,len(two)):
            dist=math.sqrt((one[k][1]-two[l][1]-round((one[k][1]-two[l][1])/xl)*xl)**2+(one[k][2]-two[l][2]-round((one[k][2]-two[l][2])/yl)*yl)**2)
              
          
            if dist<=r_cut:
                binno=int(dist/binsize)+1
                res[binno]+=2
              
    no_type2_atom=len(two)
    one.clear()
    two.clear()
f.close()    

num_density=no_type2_atom/(xl*yl)   
for i in range(len(res)):
    binvol=math.pi*((binsize*(i+1))**2-(binsize*(i))**2)/
    ans=(res[i]/(nframe*binvol*no_type2_atom)/num_density)
    gr.append(ans)    

x=[]
for i in range(len(gr)):
    x.append(binsize*i)     

x.pop()
gr.pop()
f=open(f"rdf.{filename}","w")
for i in range(len(x)):
    f.write(str(x[i])+"    "+str(gr[i])+"\n")

plt.plot(x,gr)
plt.xlabel("r/σ",style="italic",font="sans",fontsize=16)
plt.ylabel("g(r)",style="italic",font="sans",fontsize=16)
plt.savefig(f"rdffig.{filename}.png")
plt.show()

                           
