import re
import scipy
def expand(expr):
    


    symbol="^"
    r=int(expr.split(symbol)[1])
    expr=expr.replace("(","").replace(")","").replace("^"+str(r),"")
    pattern=r'([\-\+])'
    pattern2='(\d+)'
    a=re.split(pattern,expr)
    if len(a)==5:
        mf=True
        if a[3]=="-":
            ma=True
        else:
            ma=False
        x=re.split(pattern2,a[2])
        y=re.split(pattern2,a[4])
    else:
        mf=False
        if a[1]=="-":
            ma=True
        else:
            ma=False
        x=re.split(pattern2,a[0])
        y=re.split(pattern2,a[2])
    if len(x)==1:
        x1,x2=1,x[0]
    else:
        x1,x2=int(x[1]),x[2]
    if len(y)==1:
        y1,y2=1,y[0]
    else:
        y1,y2=int(y[1]),y[2]
    if r==0:
        return "1"
    else:
        if mf and ma:
            r=[((-1*y1)**(i))*((-1*x1)**(r-i))*scipy.special.comb(r,i,exact=True) for i in range(r+1)]
        else:
            if mf:
                r=[((y1)**(i))*((-1*x1)**(r-i))*scipy.special.comb(r,i,exact=True) for i in range(r+1)]
            elif ma:
                r=[((-1*y1)**(i))*((x1)**(r-i))*scipy.special.comb(r,i,exact=True) for i in range(r+1)]
            else:
                r=[(x1)**(r-i)*(y1)**(i)*scipy.special.comb(r,i,exact=True) for i in range(r+1)]
    r.reverse()
    for i in range(len(r)):
        if i!=len(r)-1 and r[i]>0:
            r[i]="+" + str(r[i])
        if i!=0:
            if i!=1:
                if r[i]==1:
                    r[i]=x2+symbol+str(i)
                elif r[i]==-1:
                    r[i]="-"+x2+symbol+str(i)
                else:
                    r[i]=str(r[i])+x2+symbol+str(i)
            else:
                if r[i]==1:
                    r[i]=x2
                elif r[i]==-1:
                    r[i]="-"+x2
                else:
                    r[i]=str(r[i]) + x2
        r[i]=str(r[i])
    r.reverse()
    return "".join(r)
