import sys
a=dict(enumerate(''.join(sys.argv[1:])))
def f(i):
 if i>80:return 1
 if'0'<a[i]:return f(i+1)
 for d in'123456789':
  if d not in[a[j]for j in a if(i//9==j//9)+(i%9==j%9)+(i//27+i%9-i%3==j//27+j%9-j%3)]:
   a[i]=d
   if f(i+1):return 1
 a[i]='0'
f(0)
for i in a:print(a[i],end='\n'*(i%9>7))
