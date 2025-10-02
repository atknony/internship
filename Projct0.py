def f0(p0) :
    v0=list(range(1,(p0+1))); v1=0; v2=0; i=0;
    while True :
        if (i<len(v0)) :
            if (v1==1 and v0[i]!=0) : v0[i]=0; v1=0;
            if (v1==0 and v0[i]!=0) : v1=1; v2+=1;
            i+=1;
        if (i==len(v0)) :
            if (v2<2) :
                for i in v0 :
                    if (i!=0) : print('final solder : ' + str(i));
                break;
            else :
                i=0; v2=0;
c0=input('initial number of solder : ');
f0(int(c0));
