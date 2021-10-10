#!/usr/bin/env python
# coding: utf-8

# #  정렬에 관련된 8문제를 풀어보았다.  
# 
# <https://www.acmicpc.net/problemset?sort=ac_desc&algo=158>   
#   
# 정렬은 병합 정렬, 분할 정복, 퀵 정렬, 힙 정렬, 계수 정렬 등 공부할 개념들이 많았다.  

# ## 2750번 수 정렬하기
# 
# <https://www.acmicpc.net/problem/2750>      
# 
# sorted를 통해 입력받은 숫자들을 오름차순으로 정렬하는 문제였다.  

# In[1]:


num=int(input())

n_list=sorted([int(input()) for i in range(num)])

for j in n_list:
    print(j)


# ## 11399번 ATM   
# 
# <https://www.acmicpc.net/problem/11399>    
# 
# total과 temp를 통해 temp에서는 n번째 사람이 걸리는 시간을 저장해주고 total에 전 사람까지 걸린 시간을 저장해주었다.

# In[11]:


people=int(input()) #사람수 입력
time=sorted(list(map(int,input().split()))) #map으로 split된 값을 list로 저장 후 sorted로 오름차순 정렬


# In[20]:


total=0 #n번째 사람까지 걸린 시간의 총합
temp=0 #n번째 사람이 기다린 시간
for i in time:
    temp=temp+i #n번째 사람이 기다린 시간= 이전 사람이 기다린 시간+ 그 사람이 걸리는 시간
    total=temp+total 
print(total)


# ## 2751번 수 정렬하기 2   
# 
# <https://www.acmicpc.net/problem/2751>    

# ###### pypy3으로 제출하면 이렇게도 해결이 된다.  

# In[8]:


num=int(input())

n_list=sorted([int(input()) for i in range(num)])

for j in n_list:
    print(j)


# ###### 하지만 python3로는 시간초과가 발생한다.  
# 이 문제는 앞에 2750번과 다르게 N의 범위가 100만까지이다. 따라서 시간복잡도 문제라고 볼 수 있다.  
# 시간복잡도를 할 수 있는 방법은 병합 정렬, 퀵 정렬, 힙 정렬이 있다.  

# ###### 병합 정렬
# 병합 정렬은 데이터를 절반씩 나누어 끝까지 갔다가 다시 절반씩 합치면서 정렬하는 방법이다.  
# 이 때 분할 단계에서 깊이가 logN에 비례하지만, 깊이별로 수행되는 merge의 시간복잡도는 O(N)이다.  
# 1. 리스트 요소가 1개가 될때까지 나눈다.  
# 2. 분리한 왼쪽리스트, 오른쪽 리스트의 각각 첫번째 요소를 비교해 더 작은 값을 결과 리스트에 저장한다.  
# 3. 저장한 값은 리스트에서 지운다.  
# 4. 두 리스트 모두 요소가 하나도 안남을 때까지 반복한다.  

# ###### 병합 정렬을 이용한 풀이
# 병합 정렬을 이용할 때는 먼저 def로 병합 정렬 함수를 만들어준다.  
# 모든 리스트 요소가 1개가 될때까지 나눈다.  
# 따라서 중간값을 기준으로 나누어주면 된다.  
# 여기서도 input 대신 sys.stdin.readline()를 사용해야한다.  

# In[85]:


import sys
n=int(input())
unsorted=[]
result=[]

# 분할
def Divided(list):
    #길이가 1일때 중단
    if len(list)<=1:
        return list
    #중간값을 기준으로 리스트 분할
    mid = len(list)//2
    less_part=list[:mid]
    more_part=list[mid:]
    less_part=Divided(less_part)
    more_part=Divided(more_part)
    return merge(less_part,more_part)

#비교와 합병
def merge(less,more):
    merged_list=[]
    l,h=0,0
    #less와 more을 돌면서 대소관계 비교 후 작은 곳에 append
    while l<len(less) and h<len(more):
        if less[l]<more[h]:
            merged_list.append(less[l])
            l=l+1
        else:
            merged_list.append(more[h])
            h=h+1
    merged_list+=less[l:]
    merged_list+=more[h:]
    return merged_list

for i in range(n):
    num=int(input())
    unsorted.append(num)

result=Divided(unsorted)

for i in result:
    print(i)


# ## 1427번 소트인사이드  
# 
# <https://www.acmicpc.net/problem/1427>   
#   
# N을 문자열로 입력받아서 각 글자들을 list에 넣고 sort를 해줘도 오름차순으로 정렬이 된다.  
# 따라서 reverse를 통해 내림차순으로 만들어주고 join으로 다시 문자열로 만들어주었다.  

# In[10]:


N=input()


# In[22]:


print(''.join(sorted([i for i in N],reverse=True)))


# ## 10989 수 정렬하기 3  
# 
# <https://www.acmicpc.net/problem/10989>  

# ###### 메모리 초과가 발생하는 코드
# sys.stdin.readline()를 사용하여도, pypy3를 사용하여도 메모리 초과가 발생한다.  
# 아마 첫째 줄에 범위가 1<=N<=10000000 까지 넓고 수 또한 10000 이하의 자연수로 매우 크기 때문이 아닐까 생각된다.  

# In[70]:


num=int(input())

n_list=sorted([int(input()) for i in range(num)])

for j in n_list:
    print(j)


# ###### 계수 정렬(counting sort) 알고리즘  
# 
# 따라서 검색을 해보니 계수 정렬 알고리즘이라는 방식이 있다고 한다.  
# 계수 정렬의 특징은
# > 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용할 수 있다.  
# > 매우 빠르다.  
# > 모든 범위를 담을 수 있는 리스트를 선언해야한다.  
# 
# 즉, 일단 범위가 되는 모든 자연수의 크기와 같은 리스트를 생성해야한다.  
# 숫자를 입력 받으면 해당하는 숫자가 나타내는 리스트 인덱스에 +1을 해주는 것이다.  
# 따라서 숫자가 입력 받았으면 1 이상이 나올 것이고 아니라면 0일 것이다.  
# 입력받은 숫자의 빈도를 물어본다면 인덱스와 값을 출력시키면 될 것이고  
# 입력받은 숫자를 정렬한다면 0이 아닌 리스트의 인덱스 값을 순서대로 출력해주면 된다.  

# ###### 계수 정렬을 이용한 풀이    
# 따라서 nlist를 통해 자연수 범위만큼 0인 리스트를 선언해주었다.  
# 그 다음 입력받은 n값을 nlist의 인덱스에서 찾아서 +1 해주었다.  
# 그 다음 nlist의 값들을 찾으면서 0보다 큰 값들만 찾아주고 그 값들의 인덱스만 추출해주면 된다.  
# 이 문제도 input을 사용하면 시간 초과가 발생한다.  

# In[69]:


#계수 정렬을 이용한 풀이
import sys
n=int(input())
nlist=[0 for i in range(10001)]

for i in range(n):
    nlist[int(input())]+=1
for i in range(len(nlist)):
    if nlist[i]>0:
        for j in range(nlist[i]):
            print(i)


# ## 11650번 좌표 정렬하기  
# 
# <https://www.acmicpc.net/problem/11650>   
# sort() 함수에서 key 파라미터에 (x,y)를 넣어주면 x를 우선 정렬해주고 y를 정렬해준다.  
# 주피터 노트북을 사용하면서 sys.stdin.readline()을 사용한 적이 없었는데 주피터 노트북에선 stdin이 잘 구현이 안된다고 한다.  
# 따라서 밑에 코드에는 input()을 사용하였지만 백준에 제출할 때는 sys.stdin.readline()으로 제출하였다.  
# input()을 하게되면 시간 초과 결과가 나오고 pypy3로 제출하면 input()을 사용해도 괜찮은 것으로 보인다.  

# In[64]:


import sys
N=input()
nlist=[]
for i in range(int(N)):
    x,y=map(int,input().split()) #실제 제출에서는 sys.stdin.readline()을 사용하였다
    nlist.append((x,y))


# In[65]:


nlist.sort(key=lambda x: (x[0],x[1]))
for j in nlist:
    print(j[0],j[1])


# ## 2309번 일곱 난쟁이  
# 
# <https://www.acmicpc.net/problem/2309>   
# 
# 이 문제는 input()을 사용하여도 시간초과는 나오지 않는다.  
# n_list에서 두 가지씩 고르는 모든 경우의 수를 찾아야하기 때문에 이중 for문을 사용하였다.  
# j는 i와 같이 않아야하기 때문에 i+1로 중복을 피했다.  
# 모든 값의 합이 100 이 되기 때문에 두 개씩 골라서 빼주었을 때 100 이 되면 그 두 값을 remove를 통해 제거하고 sorted로 내림차순 정렬한 뒤 출력해주면 된다.  
# 첫 for문이 끝나야하기 때문에 조건에 맞는 답을 골라주면 멈추면 된다.  

# In[37]:


n_list=[]
for i in range(1,10):
    tall=int(input())
    n_list.append(tall)


# In[38]:


result= sum(n_list)
for i in range(9):
    for j in range(i+1,9):
        if result-(n_list[i]+n_list[j])==100:
            a,b=n_list[i],n_list[j]
            n_list.remove(a)
            n_list.remove(b)
            n_list=sorted(n_list)
            for k in range(7):
                print(n_list[k])
            break
    if len(n_list)==7:
        break

