#!/usr/bin/env python
# coding: utf-8

# ## 우선순위 큐
# 
# <https://www.acmicpc.net/problemset?sort=ac_desc&algo=59>  
# 
# 우선순위 큐에 대해서 5문제를 풀어보았습니다.  
# 원래 7문제를 풀어야할 계획이었지만 1655,1202번을 해결하지 못했습니다.  
# 
# ## 우선순위 큐란?
# 
# 우선순위 큐는 힙이라는 자료구조와 같습니다.  
# 파이썬에서는 heapq라는 모듈을 지원해주는데 모듈에 있는 함수는 다음과 같습니다.  
# 
# 
# heapq.heappush(a,b): b를 a에 추가 - O(logn)  
# heapq.heappop(a): a에서 가장 작은 원소를 pop한 다음 리턴해주며 비어있으면 IndexError 발생 - O(logn)  
# heqpq.heapify(a): 리스트 a를 즉각적으로 heap으로 변환 - O(n) -> 만약 heappush로 만든다면? O(nlog(n))  
# 하지만 heapify는 최소 힙만을 지원합니다.  
# 
# 최소 힙이란 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리를 말합니다.  
# 최대 힙이란 각 노드의 키 값이 자식의 키 값보다 작지 않은 트리입니다.  

# ## 1927번 최소 힙  
# 
# <https://www.acmicpc.net/problem/1927>  
# 
# heapq 모듈을 이용하여 리스트에 숫자가 있을 때와 없을 때를 구분지어서 만들어줬습니다.  

# In[6]:


import heapq


hlist=[]
for i in range(int(input())):
    a=int(input())
    if len(hlist)!=0:
        if a!=0:
            heapq.heappush(hlist,a)
        else:
            b=heapq.heappop(hlist)
            print(b)
    else:
        if a!=0:
            heapq.heappush(hlist,a)
        else:
            print(a)


# ## 11279번 최대 힙  
# 
# <https://www.acmicpc.net/problem/11279>  
# 
# heapq 모듈을 이용하여 리스트에 숫자가 있을 때와 없을 때를 구분지어서 만들어줬습니다.  
# heapq는 작은 숫자를 출력하는 heappop을 지원하기 때문에 들어온 값에 -를 붙여서 저장하면 큰 수부터 출력할 수 있습니다.  

# In[11]:


import heapq

h_list=[]

for i in range(int(input())):
    a=-int(input())
    if len(h_list)==0:
        if a==0:
            print(-a)
        else:
            heapq.heappush(h_list,a)
    else:
        if a==0:
            b=heapq.heappop(h_list)
            print(-b)
        else:
            heapq.heappush(h_list,a)


# ## 11286번 절대값 힙  
# 
# <https://www.acmicpc.net/problem/11286>  
# 
# 절대값은 절대값-원래값 쌍으로 저장해주면 절대값 기준으로 첫번째 비교, 원래값으로 두번째 비교가 된다.  

# In[13]:


import heapq

for i in range(int(input())):
    a=int(input())
    if len(h_list)==0:
        if a==0:
            print(-a)
        else:
            heapq.heappush(h_list,(abs(a),a))
    else:
        if a==0:
            b=heapq.heappop(h_list)
            print(b[1])
        else:
            heapq.heappush(h_list,(abs(a),a))


# ## 1715번 카드 정렬하기  
# 
# <https://www.acmicpc.net/problem/1715>

# In[2]:


import heapq

card=[]
for i in range(int(input())): 
    a=int(input())
    heapq.heappush(card,a)

result=0
heapq.heapify(card) # 최소 힙 만들기
while len(card)>1: # 카드가 하나 이상일 때  - 적은 수끼리 계속 더하는 것이 가장 적게 걸리는 수
        a=heapq.heappop(card) #제일 작은수
        b=heapq.heappop(card) #그다음 작은 수
        heapq.heappush(card,a+b) #두개의 합
        result+=a+b 
print(result)


# ## 1766번 문제집
# 
# <https://www.acmicpc.net/problem/1766>  
# 
# '순서가 정해져 있는 작업'을 차례로 수행해야 할 때, 순서를 결정할 때 사용하는 알고리즘입니다.  
# 방향 그래프에 존재하는 각 정점들의 선행 순서를 위배하지 않으며 모든 정점을 나열하면 됩니다.  
# 하나의 방향 그래프에는 여러 개의 위상 정렬이 가능합니다.  
# 
# 위상 정렬을 만들기 위해 problem_list를 이중 리스트로 표현하는 것이 여러개의 우선 순위를 저장하기 좋다고 합니다.  
# 3개의 리스트를 만들어서 우선순위 존재 여부 확인, 우선순위에 있는 숫자들을 분리, 결과값 저장에 각각 사용하는 것이 나중에 원하는 값을 추출하기 편했습니다.  
# 

# In[8]:


import heapq


# In[12]:


problem, compare = map(int, input().split())
problem_list = [[] for i in range(problem + 1)] # 위상정렬 표현 ,index가 헷갈리지 않게 problem+1
pre = [0 for i in range(problem + 1)] #1: 우선순위가 있다.
heap = [] # 먼저 풀 문제들을 저장
result = [] # 결과값을 저장

for i in range(compare):
    a, b = map(int, input().split())
    problem_list[a].append(b) # 위상 정렬 만들기
    pre[b] += 1 #우선순위가 있다면 +1
    
print(problem_list)
print(pre)


# In[13]:


for i in range(1, problem + 1):
    if pre[i] == 0: #우선순위가 없는 것 먼저 heap에 push
        heapq.heappush(heap, i) 

while heap: # heap에 남은 것이 없을 때까지
    temp = heapq.heappop(heap) # 우선순위중 가장 작은 것 먼저 추출
    result.append(temp) 
    for j in problem_list[temp]: # 위상 정렬 만든 것에서  확인
        pre[j] -= 1 # 우선순위가 1인 것을 0으로 만들어줌-> 더이상 우선순위가 없다는 의미
        if pre[j] == 0: #우선순위가 더이상 없는 제일 작은 수를 push해줌
            heapq.heappush(heap, j)

for i in result: # 결과값 출력
    print(i, end=' ')

