from sys import argv as h
W=int(h[-1])*60
p=dict(enumerate([(0,'')]*(W+1)))
for t in h[2:-1]:
 k,z=t.split();m,s=z.split(':');v=int(m)*60+int(s)
 for w in range(W,0,-1):
  if v<=w:
   a,b=p[w];e,f=p[w-v]
   if e+v>a:p[w]=(e+v,f+k+'\n')
s,k=p[W]
print(k+f'{s//60:0>2}:{s%60:0>2}')
