
# coding: utf-8

# 条件

# In[5]:

sd1=int(raw_input('the first side:'))
sd2=int(raw_input('the second side:'))
if sd1==sd2:#注意这里的逻辑相等符号==
    print "the square's area is :%d"%(sd1*sd2)
#elif xxxxxxxx
    #print aaaaa
#elif yyyyyyy
    #print bbbbb
else:
    print "the rectangle's area is:%d"%(sd1*sd2)


# range()

# In[7]:

range(3,11,2)


# In[8]:

range(3,11)


# In[9]:

range(11)


# 递归（汉诺塔游戏）

# In[10]:

def hanoi(a,b,c,n):
    if n==1:
        print a,'->',c
    else:
        hanoi(a,c,b,n-1)
        print a,'->',c
        hanoi(b,a,c,n-1)

hanoi('a','b','c',4)


# 全局变量

# In[11]:

def f(x):
    global a
    print a
    a=5
    print a+x

a=3
f(8)
print a


#  本地文件的创建、修改

# In[24]:

f=open(r'd:\downloads\firstfile.txt','w')#创建文件


# In[25]:

f.write("Hello, world!")#写入数据


# In[26]:

f.close()#关闭文件是个好习惯


# In[28]:

f=open(r'd:\downloads\firstfile.txt','r')
p1=f.read(5)#读取前五个字符
p2=f.read()


# In[31]:

print p1,p2


# In[32]:

f.close()


# In[34]:

f=open(r'd:\downloads\companies.txt')#逐行行读取数据
cNames=f.readlines()
print cNames
f.close()


# 给每行添加序号

# In[36]:

f1=open(r'd:\downloads\companies.txt')
cNames=f1.readlines()
for i in range(0,len(cNames)):
    cNames[i]=str(i+1)+'.'+cNames[i]
f1.close()
f2=open(r'd:\downloads\scompanies.txt','w')
f2.writelines(cNames)
f2.close()


# In[40]:

s='tencent cot.'
f=open(r'd:\downloads\companies.txt','a+')
f.writelines('\n')
f.writelines(s)
f.seek(0,0)
cNames=f.readlines()
print cNames
f.close()


# 获取雅虎财经的数据

# In[1]:

from matplotlib.finance import quotes_historical_yahoo
from datetime import date
from datetime import datetime
import pandas as pd
today=date.today()
start=(today.year-1, today.month, today.day)
quotes=quotes_historical_yahoo('AXP', start, today)
fields=['date','open','close','high','low','volume']
list1=[]
for i in range(0,len(quotes)):
    x=date.fromordinal(int(quotes[i][0]))
    y=datetime.strftime(x,'%Y-%m-%d')
    list1.append(y)
quotesdf=pd.DataFrame(quotes,index=list1,columns=fields)
quotesdf=quotesdf.drop(['date'],axis=1)
print quotesdf


# #for循环

# In[2]:

s='python'
for i in s:
    print i


# In[4]:

for i in range(3,11,2):
    print i,#多个逗号不一样


# In[5]:

for i in range(3,11,2):
    print i


# 循环中的break：

# In[6]:

sumA=0
i=1
while i<=5:
    sumA+=i
    if i ==3:
        break
    print 'i=%d,sum=%d'%(i,sumA)
    i+=1


# 循环中的continue:

# In[9]:

sumA=0
i=1
while i <=5:
    sumA+=i
    i+=1
    if i==3:
        continue
    print 'i=%d,sum=%d'%(i,sumA)


# In[12]:

from random import randint
x=randint(0,300)
go='y'
while (go=='y'):
    print 'Please input a number between 0~300:'
    digit=input()
    if digit==x:
        print 'bingo!'
        break
    elif digit>x:
        print 'Too large,please try again.'
    else:
        print 'Too small,'
    print 'if you do not want to continue,input n, or input y.'
    go=raw_input()
    print go
else:
    print 'goodbye.'


# In[13]:

k=5
for i in range(1,10):
    if k==3:
        break
    else:
        print i


# 自定义函数

# In[14]:

def addMe2Me(x):
    'apply operation+to argument'#这句话告诉人这个定义的作用
    return (x+x)


# In[16]:

addMe2Me(5)


# 默认参数

# In[17]:

def f(x,y=True):#多个变量情况下，默认函数在最后
    '''x and y both correct words or not'''
    if y:
        print x,'and y both correct'
    print x,'is OK'
    


# In[18]:

f(99)


# 传递函数

# In[19]:

def addMe2Me(x):
    return(x+x)
def self(f,y):
    print f(y)


# In[20]:

self(addMe2Me,2.2)


# lambda函数

# In[22]:

r=lambda x:x+x
r(5)


# In[23]:

#等价于
def my_add(x,y):return x+y
lambda x,y:x+y
my_add(5,5)


# In[ ]:



