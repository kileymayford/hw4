import matplotlib.pyplot as plt
import math
K=0.5
p_o=0
p_n=p_o
q_o=math.pi/4
p_m=0
q_m=0
n=0
q_n=q_o
pn=[]
pm=[]
qn=[]
qm=[]
n_max=100
count=5
ax=plt.subplot(111)

while n<n_max:
   p_m=p_n-K*math.sin(q_n)
   q_m=q_n+p_m
   pn.append(p_n)
   pm.append(p_m)
   qn.append(q_n)
   qm.append(q_m)
   p_n=p_m
   q_n=q_m
   n +=1
   if n==n_max:
     # plt.scatter(pn,pm,label="p")
     # plt.scatter(qn,qm, label="q")
     # plt.legend()
      if K==2:
         print(K,p_o)
         if p_o==math.pi/4:
            plt.scatter(pn,pm,label="p$_o$=pi/4 K=2")
            plt.scatter(qn,qm, label="q$_o$=0 K=2")
            plt.legend(loc='center right',bbox_to_anchor=(1.1,.5))
            plt.savefig('K2-ppi.pdf')
            n=n_max+1
         if p_o==0:
            p_o=math.pi/4
            q_o=0
            count=0
            n=0
            plt.scatter(pn,pm,label="p$_o$=0 K=2")
            plt.scatter(qn,qm, label="q$_o$=pi/4 K=2")
            plt.legend(loc='center left',bbox_to_anchor=(1.1,1.05))
            plt.savefig('K2-p0.pdf')
      if K==1:
         print(K,p_o)
         if p_o==0:
            plt.scatter(pn,pm,label="p$_o$=0 K=1")
            plt.scatter(qn,qm, label="q$_o$=pi/4 K=1")
            plt.legend(loc='center left',bbox_to_anchor=(1.1,1.05))
            plt.savefig('K1-p0.pdf')
         if p_o==math.pi/4:
            plt.scatter(pn,pm,label="p$_o$=pi/4 K=1")
            plt.scatter(qn,qm, label="q$_o$=0 K=1")
            plt.legend(loc='center left',bbox_to_anchor=(1.1,1.05))
            plt.savefig('K1-ppi.pdf')
         K=2
         n=0
      if K==0.5:
         print(K,p_o)
         K=1
         n=0
         if p_o==0:
            plt.scatter(pn,pm,label="p$_o$=0 K=0.5")
            plt.scatter(qn,qm, label="q$_o$=pi/4 K=.5")
            plt.legend(loc='center left',bbox_to_anchor=(1.1,1.05))
            plt.savefig('K05-p0.pdf')
         if p_o==math.pi/4:
            plt.scatter(pn,pm,label="p$_o$=pi/4 K=0.5")
            plt.scatter(qn,qm, label="q$_o$=0 K=0.5")
            ax.legend(loc='center left',bbox_to_anchor=(1.1,1.05))
            plt.savefig('K05-ppi.pdf')
      if count==0:
         K=0.5
         count=1
      p_m=0
      q_m=0
      q_n=q_o
      p_n=p_o
      #print(pn)
      del pn[:]
      del pm[:]
      del qn[:]
      del qm[:]

