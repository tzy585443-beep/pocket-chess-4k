# SPDX-License-Identifier: MIT
import time;N=-10;D=N,-1,1,10,-11,-9,9,11;R,B=D[:4],D[4:];K=-21,-19,-12,-8,8,12,19,21;Y=dict(N=K,B=B,R=R,Q=D,K=D,P=(N,-20,-11,-9));V=dict(P=100,N=320,B=330,R=500,Q=900,K=0);Z=' '*9+'\n'
class G(Exception):[]
F=lambda b:''.join(b[i:i+10]for i in range(110,-1,-10)).swapcase()
def A(b,k):
 if any(b[k+d]=='n'for d in K)or'p'in(b[k-9],b[k-11]):return 1
 for d in D:
  j=k+d;q=b[j]
  if q=='k':return 1
  while q=='.':j+=d;q=b[j]
  if q=='q'or q=='r'and d in R or q=='b'and d in B:return 1
 return 0
def J(b,w,e):
 for i,p in enumerate(b):
  if not p.isupper():continue
  for d in Y[p]:
   j=i+d
   while 1:
    q=b[j]
    if q<'.'or q.isupper():break
    if p=='P'and(q!='.'or d==N+N and(i<81 or b[i+N]!='.')if d in(N,N+N)else q=='.'and j!=e):break
    yield i,j,'Q'*(p=='P'and j<30)
    if p in'PNK'or q>'Z':break
    if i in(91,98)and w>>(k:=i>95)&1 and b[j+1-2*k]=='K'and not A(b,95)+A(b,94+2*k)+A(b,93+4*k):yield 95,93+4*k,''
    j+=d
def U(b,w,e):
 return[m for m in J(b,w,e)if not A((s:=Q(b,w,w,e,m,0)),s.index('K'))]
def Q(b,w,c,e,m,fl=1):
 i,j,r=m;n=[*b];p=n[i];n[i]='.';n[j]=r or p
 if p=='P'and j==e:n[j+10]='.'
 if p=='K'and abs(j-i)==2:n[98-7*(j<i)]='.';n[96-2*(j<i)]='R'
 if not fl:return n
 w&=~3 if p=='K'else~((i==91 or j==91)+2*(i==98 or j==98));c&=~((j==21)+2*(j==28));return F(''.join(n)),c,w,(i+N)%10+110-(i+N)//10*10 if p=='P'and j-i==N*2 else 0
def E(b):
 s=0
 for i,c in enumerate(b):
  if c>'@':u=c.upper();r=i//10;r=9-r if u==c else r-2;s+=(V[u]+(r if u=='P'else 4-abs(r-3))*6)*(1-2*(u!=c))
 return s
def M(b,m,tm,p):
 if m==tm:return 1e7
 i,j,r=m;q=b[j]
 if q>'Z'or r:return 2e4+9*V.get(q.upper(),0)-V[b[i]]
 return G.h.get((b[i],j),0)+(m==G.k.get(p))*5e3
def S(b,w,c,e,a,B,d,p=0,n=1):
 if time.time()>G.dl:raise G
 ic=A(b,b.index('K'));q=d<1;g=q and ic<1;s=E(b)if g else 0
 if g and s>=B:return s
 if g:a=max(a,s)
 z=b,w,c,e;t=G.tt.get(z)if d else 0
 if t and t[0]>=d and p and not t[1]:return t[2]
 L=[m for m in U(b,w,e)if q<=ic or m[2]or b[m[1]]>'Z'or m[1]==e]
 if not L:return p-3e4 if ic else s if q else 0
 L.sort(key=lambda m:-M(b,m,t and t[3],p))
 if n*p*d>2 and ic<1 and -S(F(b),c,w,0,-B,1-B,d-3,p+1,0)>=B:return B
 bs,bm,a0=(s if g else -4e4),L[0],a
 for i,m in enumerate(L):
  qt=b[m[1]]=='.'and not m[2];u=Q(b,w,c,e,m);nd=d-1 if d else 0;ww=i and nd
  v=-S(*u,-a-1 if ww else -B,-a,nd-ww*(i>3)*(nd>2)*qt,p+1)
  if ww and a<v<B:v=-S(*u,-B,-a,nd,p+1)
  if v>bs:bs,bm=v,m
  a=max(a,v)
  if a>=B:
   if d*qt:G.k[p]=m;h=b[m[0]],m[1];G.h[h]=G.h.get(h,0)+d*d
   break
 if d:G.tt[z]=d,(bs>=B)-(bs<=a0),bs,bm
 return bs
def H(m,s):
 return''.join(chr(96+i%10)+str((10-i//10,i//10-1)[not s])for i in m[:2])+m[2].lower()
def O(u,s):
 z=lambda x:(10-int(x[1]),int(x[1])+1)[not s]*10+ord(x[0])-96;return z(u[:2]),z(u[2:4]),u[4:].upper()
def X(t):
 i=t.index('moves')if'moves'in t else len(t);f=t[2:i]if t[1]=='fen'else['rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR','w','KQkq','-'];s=f[0]
 for n in'87654321':s=s.replace(n,'.'*int(n))
 b=Z*2+' '+'\n '.join(s.split('/'))+'\n'+Z*2;C=f[2];w=2*('K'in C)+('Q'in C);c=2*('k'in C)+('q'in C);x=f[3];e=x!='-'and(10-int(x[1]))*10+ord(x[0])-96
 if f[1]=='b':b,w,c,e=F(b),c,w,e and e%10+110-e//10*10
 o=f[1]=='w'
 for u in t[i+1:]:b,w,c,e=Q(b,w,c,e,O(u,o));o^=1
 return b,w,c,e,o
def I(b,w,c,e,o,g):
 G.h,G.k,G.tt={},{},{};L=U(b,w,e)
 if not L:return'0000'
 L.sort(key=lambda m:-M(b,m,0,0));z=L[0];k='bw'[o];d=dict(zip(g,g[1:]));N=lambda x,f=0:int(d[x])if x in d else f;r=N('movetime')or N(k+'time',800);h=0 if r<40 else min(r-20,r if N('movetime') else r//16+N(k+'inc'))
 if h<1:return H(z,o)
 G.dl=time.time()+h/1e3
 try:
  for d in range(1,8):
   S(b,w,c,e,-4e4,4e4,d);t=G.tt.get((b,w,c,e))
   if t and t[3]:z=t[3]
 except G:[]
 return H(z,o)
def W(s):print(s,flush=1)
def main():
 st=None
 for ln in open(0):
  p=ln.split()
  if not p:continue
  x=p[0]
  if x=='uci':W('uciok')
  elif x=='isready':W('readyok')
  elif x=='ucinewgame':st=None
  elif x=='position':st=X(p)
  elif x=='quit':break
  elif x=='go':st=st or X(['position','startpos']);W('bestmove '+I(*st,p))
if __name__=='__main__':main()
