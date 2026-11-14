# SPDX-License-Identifier: MIT
import time
N=-10
D=N,-1,1,10,-11,-9,9,11
R,B=D[:4],D[4:];K=(-21,-19,-12,-8,8,12,19,21);Y=dict(N=K,B=B,R=R,Q=D,K=D,P=(N,-20,-11,-9))
V=dict(P=100,N=320,B=330,R=500,Q=900,K=0)
Z=' '*9+'\n';I=Z*2+' rnbqkbnr\n pppppppp\n'+' ........\n'*4+' PPPPPPPP\n RNBQKBNR\n'+Z*2
class G(Exception):pass
def tk():
 G.n+=1
 if G.n>=G.cap or G.n&31==0 and time.time()>G.dl:raise G
F=lambda b:''.join(b[i:i+10]for i in range(110,-1,-10)).swapcase()
def A(b,k):
 if any(b[k+d]=='n'for d in K):return 1
 for d in D:
  j=k+d;q=b[j]
  if q=='k':return 1
  while q=='.':j+=d;q=b[j]
  if q=='q'or q=='r'and d in R or q=='b'and d in B:return 1
 return'p'in(b[k-9],b[k-11])
def gn(b,w,e):
 for i,p in enumerate(b):
  if not p.isupper():continue
  for d in Y[p]:
   j=i+d
   while 1:
    q=b[j]
    if q<'.'or q.isupper():break
    if p=='P'and(d in(N,N+N)and q!='.'or d==N+N and(i<81 or b[i+N]!='.')or abs(d+10)==1 and q=='.'and j!=e):break
    yield (i,j,'Q')if p=='P'and j<30 else(i,j,'')
    if p in'PNK'or q>'Z':break
    if i in(91,98)and w&(1+(i>95))and b[j+1-2*(i>95)]=='K'and not A(b,95)+A(b,94+2*(i>95))+A(b,93+4*(i>95)):yield 95,93+4*(i>95),''
    j+=d
def lg(b,w,e):
 return[m for m in gn(b,w,e)if not A((s:=mk(b,w,w,e,m,0)),s.index('K'))]
def mk(b,w,c,e,m,fl=1):
 i,j,r=m;n=[*b];p=n[i];n[i]='.';n[j]=r or p
 if p=='P'and j==e:n[j+10]='.'
 if p=='K'and abs(j-i)==2:n[98-7*(j<i)]='.';n[96-2*(j<i)]='R'
 s=''.join(n)
 if not fl:return s
 w=0 if p=='K'else w&~(i==91 or j==91)&~(2*(i==98 or j==98))
 c&=~(j==21)&~(2*(j==28))
 return F(s),c,w,(i+N)%10+110-(i+N)//10*10 if p=='P'and j-i==N*2 else 0
def ev(b):return sum(V.get(c,-V.get(c.upper(),0))for c in b)
def ok(b,m,tm,p):
 if m==tm:return 1e7
 i,j,r=m;q=b[j]
 if q>'Z':return 9*V.get(q.upper(),100)-V[b[i]]
 return G.h.get((b[i],j),0)+(m in G.k.get(p,()))*5000
def ab(b,w,c,e,a,B,d,p=0,nm=1):
 tk();ic=A(b,b.index('K'));q=d<1;s=ev(b)if q and ic<1 else 0
 if q and ic<1:
  if s>=B:return s
  a=max(a,s)
 z=b,w,c,e;t=d>0 and G.tt.get(z)
 if t and t[0]>=d and p and(t[1]==0 or t[1]>0 and t[2]>=B or t[1]<0 and t[2]<=a):return t[2]
 L=[m for m in lg(b,w,e)if q<1 or ic or m[2]or b[m[1]]>'Z'or m[1]==e]
 if not L:return p-3e4 if ic else s if q else 0
 L.sort(key=lambda m:-ok(b,m,t and t[3],p))
 if nm*d>2 and p and ic<1 and -ab(F(b),c,w,0,-B,1-B,d-3,p+1,0)>=B:return B
 bs,bm,a0=(s if q and ic<1 else -4e4),L[0],a
 for i,m in enumerate(L):
  qt=b[m[1]]=='.'and not m[2];u=mk(b,w,c,e,m);nd=d-1 if d>0 else 0
  v=-ab(*u,-a-1,-a,nd-(i>3)*(nd>2)*qt,p+1)if i and nd else -ab(*u,-B,-a,nd,p+1)
  if i and nd and a<v<B:v=-ab(*u,-B,-a,nd,p+1)
  if v>bs:bs,bm=v,m
  if v>a:a=v
  if a>=B:
   if d*qt:G.k[p]=((m,)+G.k.get(p,()))[:2];G.h[b[m[0]],m[1]]=G.h.get((b[m[0]],m[1]),0)+d*d
   break
 if d>0:G.tt[z]=(d,(bs>=B)-(bs<=a0),bs,bm)
 return bs
def fm(m,s):
 z=lambda i:'abcdefgh'[i%10-1]+str((10-i//10,i//10-1)[not s]);return z(m[0])+z(m[1])+m[2].lower()
def pu(u,s):
 z=lambda x:(10-int(x[1]),int(x[1])+1)[not s]*10+ord(x[0])-96;return z(u[:2]),z(u[2:4]),u[4:].upper()
def ld(tk):
 b,w,c,e,sd=I,3,3,0,1
 if'moves'in tk:
  for u in tk[tk.index('moves')+1:]:b,w,c,e=mk(b,w,c,e,pu(u,sd));sd^=1
 return b,w,c,e,sd
def pg(p):
 d,i={},1
 while i<len(p):
  if i+1<len(p)and p[i]in('wtime','btime','movetime'):d[p[i]]=int(p[i+1]);i+=2
  else:i+=1
 return d
def th(b,w,c,e,sd,go):
 G.h={};G.k={};L=sorted(lg(b,w,e),key=lambda m:-ok(b,m,0,0))
 if not L:return'0000'
 best=L[0];mt=go.get('movetime');rem=mt or go.get(('btime','wtime')[sd],1e6);now=time.time()
 hard=min(200,rem*.15)
 G.dl=now+hard/1e3;G.cap=int(hard*3)+1;G.n=0;G.tt={}
 try:
  for d in range(1,8):
   if d>1 and time.time()>G.dl:break
   sc=ab(b,w,c,e,-4e4,4e4,d);t=G.tt.get((b,w,c,e))
   if t and t[3]:best=t[3]
   if abs(sc)>2e4:break
 except G:pass
 return fm(best,sd)
def W(s):print(s,flush=1)
def main():
 st=None
 for ln in open(0):
  p=ln.split()
  if not p:continue
  x=p[0]
  if x=='uci':W('uciok')
  elif x=='isready':W('readyok')
  elif x=='position'and'startpos'in p:st=ld(p)
  elif x=='go':st=st or ld(['startpos']);W('bestmove '+th(*st,pg(p)))
if __name__=='__main__':main()
