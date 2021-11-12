#!/usr/bin/env python
# coding: utf-8

# # 큐에 관련된 6문제를 풀어보았다.  
# 
# <https://www.acmicpc.net/problemset?sort=ac_desc&algo=72>
# 
# 3190번 뱀을 풀지 못했다...

# # 큐란?
# 
# 큐는 선입선출의 개념이다.  

# ## 10845번 큐  
# 
# <https://www.acmicpc.net/problem/10845>  
# 
# 이전에 풀었던 스택에서와 유사한 문제이다.  
# 먼저 명령어를 입력받았고 그 명령에 'push'가 있다면 띄어쓰기를 기준으로 나누어 que_list에 추가해주었다.  
# 제일 앞에 숫자를 추출하는 것은 list의 index를 사용하였다.  

# In[8]:


que_list=[]
for i in range(int(input())):
    command=input()
    if 'push' in command:
        a,b=command.split()
        que_list.append(b)
    if 'front' in command:
        if len(que_list)==0:
            print('-1')
        else:
            print(que_list[0])
    if 'back' in command:
        if len(que_list)==0:
            print('-1')
        else:
            print(que_list[-1])
    if 'pop' in command:
        if len(que_list)==0:
            print('-1')
        else:
            a=que_list[0]
            que_list.remove(a)
            print(a)
    if 'size' in command:
        print(len(que_list))
    if 'empty' in command:
        if len(que_list)==0:
            print('1')
        else:
            print('0')


# ## 1158번 요세푸스 문제  
# 
# <https://www.acmicpc.net/problem/1158>  
# 
# 먼저 N개의 숫자가 들어가있는 que 리스트를 만들고 que에서 빠질 숫자들을 저장하는 result 리스트를 만들었습니다.
# num을 통해 que의 인덱싱을 조절해줍니다.
# 하나의 숫자가 que에서 빠지면 뒤에 숫자가 그 빠진 위치에 들어오기 때문에 num은 K-1 만큼 더해줬습니다.
# num이 que의 인덱스 범위에 벗어나게 되면 처음으로 돌아가야하고 그 숫자는 num/len(que)의 나머지가 됩니다.
# 그렇게 반복문으로 나온 순서대로 result에 append 시켜주면 문제는 해결됩니다.
# 마지막으로 ‘[]’가 아닌 ‘<>’로 묶여있기 때문에 리스트 전체를 문자열로 만들어서 ‘[]’를 ‘<>’로 replace를 통해 바꿔주었습니다.

# In[61]:


N,K=map(int,input().split())
result=[]
num=0
que=[]
for i in range(1,N+1):
    que.append(i)

for i in range(N):
    num=num+K-1
    if num >=len(que):
        num=num%len(que)
    result.append(que.pop(num))
result=str(result)
result=result.replace('[','<')
result=result.replace(']','>')
print(result)


# ## 1966번 프린터 큐 
# 
# <https://www.acmicpc.net/problem/1966>  
# 
# 목표하는 index 값을 'target'으로 바꿔서 처리하기 수월했다.  
# pop으로 숫자를 꺼내서 뒤에 append를 추가하였다.  

# In[16]:


test_cases = int(input())

for _ in range(test_cases):
    n,m = list(map(int, input().split( )))
    prior = list(map(int, input().split( )))
    index = list(range(len(prior)))
    index[m] = 'target'
    order = 0
    
    while True:
        if prior[0]==max(prior):
            order += 1
            if index[0]=='target':
                print(order)
                break
            else:
                prior.pop(0)
                index.pop(0)
        else:
            prior.append(prior.pop(0))
            index.append(index.pop(0))


# ## 2164번 카드 2 
# 
# <https://www.acmicpc.net/problem/2164>  
# 
# deque를 이용해서 한번은 숫자를 없애고 한번은 뒤로 append해주고 남은 하나의 숫자를 출력하면 된다.  

# In[29]:


import sys
from collections import deque

card=deque()
for i in range(int(input())):
    card.append(i+1)
    
while len(card) != 1:
    card.popleft()
    a=card.popleft()
    card.append(a)
print(card[0])


# ## 11866번 요세푸스 문제 0  
# 
# <https://www.acmicpc.net/problem/11866>  
# 
# 위에 문제와 같이 풀어도 됐다...

# In[30]:


N,K=map(int,input().split())
result=[]
num=0
que=[]
for i in range(1,N+1):
    que.append(i)

for i in range(N):
    num=num+K-1
    if num >=len(que):
        num=num%len(que)
    result.append(que.pop(num))
result=str(result)
result=result.replace('[','<')
result=result.replace(']','>')
print(result)


# ## 3190번 뱀 
# 
# <https://www.acmicpc.net/problem/3190>

# In[100]:


n=int(input())
board=[[0]*n for i in range(n)]
print(board)


# In[101]:


K=int(input())
for i in range(K):
    a,b=map(int,input().split())
    board[a-1][b-1]=1
print(board)


# ## 18258번 큐 2
# 
# <https://www.acmicpc.net/problem/18258>  
# 
# 위에서 list와 인덱싱을 통해 처리했던 문제를 deque를 통해서 시간을 절약하는 문제이다.  

# In[32]:


import sys
from collections import deque

que_list=deque()
for i in range(int(input())):
    command=input()
    if 'push' in command:
        a,b=command.split()
        que_list.append(b)
    if 'front' in command:
        if len(que_list)==0:
            print('-1')
        else:
            print(que_list[0])
    if 'back' in command:
        if len(que_list)==0:
            print('-1')
        else:
            print(que_list[-1])
    if 'pop' in command:
        if len(que_list)==0:
            print('-1')
        else:
            print(que_list.popleft())
    if 'size' in command:
        print(len(que_list))
    if 'empty' in command:
        if len(que_list)==0:
            print('1')
        else:
            print('0')

